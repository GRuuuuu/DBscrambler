import re
import random
import datetime
from korean_name_generator import namer
from faker import Faker
import argparse
import names
import string
import lorem

adr_meta = ['ZIP_NO', 'SIDO', 'SIDO_ENG', 'SIGUNGU', 'SIGUNGU_ENG', 'EUPMYUN', 'EUPMYUN_ENG',
            'DORO_CD', 'DORO', 'DORO_ENG', 'UNDERGROUNT_YN', 'BUILD_NO1', 'BUILD_NO2', "BUILD_NO_MANAGE_NO",
            'DARYANG_NM', 'BUILD_NM', 'DONG_CD', 'DONG_NM', 'RI', 'H_DONG_NM', 'SAN_YN', 'ZIBUN1',
            'EUPMYUN_DONG_SN', 'ZIBUN2', 'ZIP_NO_OLD', 'ZIP_SN']
zipcode_path='random_zipcodeKR.txt'

class DBScramble:
    def __init__(self,
                 dumpfile='test_dump.sql',
                 infofile='convert_info.yml',
                 outfile_scrambled='out_scrambled.sql',
                 outfile_blank='out_blank.sql'):
        self.state = "none"
        self.dumpfile = dumpfile
        self.outfile_scrambled = outfile_scrambled
        self.outfile_blank = outfile_blank
        self.infofile = self.load_yaml(infofile)
        self.dbname = list(self.infofile.keys())[0]
        self.zipcode_kr = open(zipcode_path)
        self.faker_en = Faker()
        self.faker_kr = Faker('ko-KR')

    def load_yaml(self, infofile):
        import yaml
        with open(infofile) as f:
            infofile = yaml.load(f, Loader=yaml.FullLoader)
        infofile = {
            db['name']: {
                item['name']: [(details['column'], details['cvt_option'],
                                details['params'] if 'params' in details.keys() else None)
                               for details in item['object_list']]
                            for item in db['tables']}
                        for db in infofile['dbs']
        }
        return infofile

    def set_state(self, state):
        self.state = state

    # convert action functions
    def cvt_option_function(self):
        pass

    def fake_eng_sentence(self):
        return '\'' + random.choice([lorem.sentence()[:30], '']) + '\''

    def fake_email(self):
        return '\'' + self.faker_en.email() + '\''

    def fake_ip(self):
        return '\'' + self.faker_en.ipv4() + '\''

    def korean_name(self):
        return '\'' + random.choice([namer.generate(True), namer.generate(False)]) + '\''

    def english_name(self):
        return '\'' + names.get_full_name() + '\''

    def phone_withdash(self, front_3dgits):
        if front_3dgits.startswith('02'):
            return '\'' + '02' + "-" + str(random.randint(0, 9999)).zfill(4) + "-" + str(random.randint(0, 9999)).zfill(
            4) + '\''
        else:
            return '\'' + front_3dgits + "-" + str(random.randint(0, 9999)).zfill(4) + "-" + str(random.randint(0, 9999)).zfill(
            4) + '\''

    def phone_nodash(self, front_3dgits):
        if front_3dgits.startswith('02'):
            return '\'' + '02' + str(random.randint(0, 9999)).zfill(4) + str(random.randint(0, 9999)).zfill(
                4) + '\''
        else:
            return '\'' + front_3dgits + str(random.randint(0, 9999)).zfill(4) + str(random.randint(0, 9999)).zfill(
                4) + '\''



    def fake_emp(self):
        return '\'' + ''.join(random.choice(string.digits) for _ in range(4)) + '\''

    def fake_member(self):
        return '\'' + ''.join(random.choice(string.digits) for _ in range(14)) + '\''

    def random_adress(self):
        pass

    def random_string(self, **params):
        string_set = ''
        if 'digit' in params['object']:
            string_set += string.digits
        if 'en_lowercase' in params['object']:
            string_set += string.ascii_lowercase
        if 'en_uppercase' in params['object']:
            string_set += string.ascii_uppercase
        if 'symbol' in params['object']:
            string_set += string.punctuation.replace('\'', '')
        if 'blank' in params['object']:
            string_set += ' '
        ret = '\'' + ''.join(random.choice(string_set) for _ in range(params['length'])) + '\''
        return ret
        # if object == 'digit':
        #     ret = '\'' + ''.join(random.choice(string.digits) for _ in range(length)) + '\''
        # return ret

    def set_string(self, **params):
        string='\'' + params['string'] + '\''
        return string

    def fake_kor_address(self):
        # fake = Faker('ko-KR')
        return '\'' + self.faker_kr.address() + '\''

    def fake_kor_zipcode(self):
        # fake = Faker('ko-KR')
        return '\'' + self.faker_kr.postcode() + '\''

    def fake_eng_address(self):
        # fake = Faker()
        return '\'' + self.faker_en.address() + '\''

    def fake_eng_zipcode(self):
        # fake = Faker()
        return '\'' + self.faker_en.postcode() + '\''

    def fake_account(self):
        return '\'' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '\''

    def fake_birth(self):
        start_date = datetime.date(1900, 1, 1)
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        yymmdd = str(random_date.year) + str(random_date.month).zfill(2) + str(random_date.day).zfill(2)
        return '\'' + yymmdd + '\''

    def rand_nice_no(self):
        return str(random.randint(10000, 99999))

    def kr_zipcode(self, address):
        return '\'' + address[adr_meta.index('ZIP_NO')] + '\''

    def kr_doro(self, address):
        return '\'' + address[adr_meta.index('SIDO')] + ' ' + address[adr_meta.index('SIGUNGU')] + ' ' + address[
            adr_meta.index('DORO')] + '\''

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

    # convert job in line
    def convert(self, _line, infofile, target_table, table2cols, option):
        _line = _line[0].split(',')
        for name, func, params in infofile[self.dbname][target_table]:
            if option == 'scrambled':
                element = _line[table2cols[target_table].index(name)]
                if params is None:
                    if func in ['phone_withdash','phone_nodash']:
                        front_3digit = element[1:4]
                        if element.lower() not in ['null'] and element.strip('\'') not in ['Removed', '']:
                            _line[table2cols[target_table].index(name)] = eval('self.' + func)(front_3digit)
                    else:
                        if element.lower() not in ['null'] and element.strip('\'') not in ['Removed', '']:
                            _line[table2cols[target_table].index(name)] = eval('self.' + func)()
                elif func == 'random_address':
                    fullAdr = self.zipcode_kr.readline()
                    if fullAdr is None:
                        self.zipcode_kr = open(zipcode_path)
                        fullAdr = self.zipcode_kr.readline()
                    address = fullAdr.split('|')
                    for each in params:
                        _element = _line[table2cols[target_table].index(each['column'])]
                        if _element.lower() not in ['null'] and _element.strip('\'') not in ['Removed', '']:
                            _line[table2cols[target_table].index(each['column'])] = eval('self.' + each['cvt_option'])(address)
                else:
                    _params = {}
                    for each in params:
                        _params.update(each)
                    if element.lower() not in ['null'] and element.strip('\'') not in ['Removed', '']:
                        _line[table2cols[target_table].index(name)] = eval('self.' + func)(**_params)
            elif option == 'blank':
                _line[table2cols[target_table].index(name)] = ''
        _line = '(' + ','.join(_line) + ')'
        return _line

    # parsing via line-by-line
    def parse(self):
        table2cols = dict()
        out_scrambled = open(self.outfile_scrambled, 'w')
        out_blank = open(self.outfile_blank, 'w')
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
                    out_scrambled.write(line)
                    out_blank.write(line)
                elif self.state == "create table":
                    if line.strip().lower().startswith('`'):
                        col = re.findall('\`.*?\`', line)[0].strip('`')
                        table2cols[target_table].append(col)
                    if line.strip().endswith(';'):
                        self.set_state('none')
                    out_scrambled.write(line)
                    out_blank.write(line)
                elif self.state == "insert table":
                    l = re.findall("\((.+)\)", line)
                    if l:
                        _line_scrambled = self.convert(l, self.infofile, target_table, table2cols, option='scrambled')
                        _line_blank = self.convert(l, self.infofile, target_table, table2cols, option='blank')
                        if line.endswith(';\n'):
                            self.set_state("none")
                            out_scrambled.write(_line_scrambled + ';\n')
                            out_blank.write(_line_blank + ';\n')
                        elif line.endswith(',\n'):
                            out_scrambled.write(_line_scrambled + ',\n')
                            out_blank.write(_line_blank + ',\n')
                        elif line.endswith('\n'):
                            out_scrambled.write(_line_scrambled + '\n')
                            out_blank.write(_line_blank + '\n')
                    else:
                        if line.endswith(';\n'):
                            self.set_state("none")
                            out_scrambled.write(line)
                            out_blank.write(line)
        out_scrambled.close()
        out_blank.close()


parser = argparse.ArgumentParser(description='convert or validate sqldump file')
parser.add_argument('--file', type=str, default=None)
parser.add_argument('--input', type=str, default=None)
parser.add_argument('--output_scrambled', type=str, default=None)
parser.add_argument('--output_blank', type=str, default=None)
args = parser.parse_args()

masker = DBScramble(dumpfile=args.input,
                    infofile=args.file,
                    outfile_scrambled=args.output_scrambled,
                    outfile_blank=args.output_blank)
masker.parse()
