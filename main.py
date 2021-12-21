import re
import random
import datetime
from korean_name_generator import namer
from faker import Faker
import argparse


class DBScramble:
    def __init__(self,
                 dumpfile='test_dump.sql',
                 infofile='convert_info.yml',
                 outfile='out.sql'):
        self.state = "none"
        self.dumpfile = dumpfile
        self.outfile = outfile
        self.infofile = self.load_yaml(infofile)
        self.dbname = list(self.infofile.keys())[0]

    def load_yaml(self, infofile):
        import yaml
        with open(infofile) as f:
            infofile = yaml.load(f, Loader=yaml.FullLoader)

        infofile = {
            infofile['db']: {
                item['name']: [(details['column'], details['cvt_option'])
                               for details in item['object_list']]
                for item in infofile['tables']}
        }
        return infofile

    def set_state(self, state):
        self.state = state

    def korean_name(self):
        return '\'' + random.choice([namer.generate(True), namer.generate(False)]) + '\''

    def korean_phone(self):
        return '\'' + "010-" + str(random.randint(0, 9999)).zfill(4) + "-" + str(random.randint(0, 9999)).zfill(
            4) + '\''

    def korean_address(self):
        fake = Faker('ko-KR')
        return '\'' + fake.address() + '\''

    def korean_rid(self):
        start_date = datetime.date(1900, 1, 1)
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        yymmdd = str(random_date.year % 100).zfill(2) + str(random_date.month).zfill(2) + str(random_date.day).zfill(2)

        back = str(random.randint(1, 4)) + str(random.randint(0, 96)).zfill(2) + str(random.randint(0, 99)).zfill(
            2) + str(random.randint(1, 9))
        # 5. 주문배송정보 및 상담->Personal Information 주의
        check = 0
        for each, mul in zip(yymmdd + back, list(range(2, 10)) + list(range(2, 6))):
            check += int(each) * mul
        last = 11 - check % 11
        id = yymmdd + '-' + back + str(last)[0]
        return '\'' + id + '\''

    def convert(self, _line, infofile, target_table, table2cols):
        _line = _line[0].split(',')
        for name, func in infofile[self.dbname][target_table]:
            _line[table2cols[target_table].index(name)] = eval('self.' + func)()
        _line = '(' + ','.join(_line) + ')'
        return _line

    def validate(self):
        pass

    def parse(self, func='convert'):
        table2cols = dict()
        out = open(self.outfile, 'w')
        with open(self.dumpfile, 'rb') as f:
            for line in f:
                line = line.decode('UTF-8')
                if self.state == "none":
                    if line.strip().lower().startswith('create table'):
                        table = re.findall('\`.*?\`', line)[0].strip('`')
                        if table in self.infofile[self.dbname].keys():
                            self.set_state('create table')
                            target_table = table
                            table2cols[target_table] = []
                    if line.strip().lower().startswith('insert into'):
                        table = re.findall('\`.*?\`', line)[0].strip('`')
                        if table in self.infofile[self.dbname].keys():
                            self.set_state('insert table')
                            target_table = table
                    out.write(line)
                elif self.state == "create table":
                    if line.strip().lower().startswith('`'):
                        col = re.findall('\`.*?\`', line)[0].strip('`')
                        table2cols[target_table].append(col)
                    if line.strip().endswith(';'):
                        self.set_state('none')
                    out.write(line)
                elif self.state == "insert table":
                    if func == 'convert':
                        l = re.findall("\((.+)\)", line)
                        if l:
                            _line = self.convert(l, self.infofile, target_table, table2cols)
                            if line.endswith(';\n'):
                                self.set_state("none")
                                out.write(_line+';\n')
                            elif line.endswith(',\n'):
                                out.write(_line+',\n')
                            elif line.endswith('\n'):
                                out.write(_line+'\n')
                        else:
                            if line.endswith(';\n'):
                                self.set_state("none")
                                out.write(line)
                    elif func == 'validate':
                        # def validate function with self.infofile, target_table, table2cols
                        self.validate()
        out.close()


parser = argparse.ArgumentParser(description='convert or validate sqldump file')
parser.add_argument('--func', type=str, default=None)
parser.add_argument('--file', type=str, default=None)
parser.add_argument('--input', type=str, default=None)
parser.add_argument('--output', type=str, default=None)
args = parser.parse_args()

masker = DBScramble(dumpfile=args.input, infofile=args.file, outfile=args.output)
masker.parse(func=args.func)
