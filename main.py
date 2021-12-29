import re
import random
import datetime
from korean_name_generator import namer
from faker import Faker
import argparse
import names
import string

adr_meta = ['ZIP_NO', 'SIDO', 'SIDO_ENG', 'SIGUNGU', 'SIGUNGU_ENG', 'EUPMYUN', 'EUPMYUN_ENG',
            'DORO_CD', 'DORO', 'DORO_ENG', 'UNDERGROUNT_YN', 'BUILD_NO1', 'BUILD_NO2', "BUILD_NO_MANAGE_NO",
            'DARYANG_NM', 'BUILD_NM', 'DONG_CD', 'DONG_NM', 'RI', 'H_DONG_NM', 'SAN_YN', 'ZIBUN1',
            'EUPMYUN_DONG_SN', 'ZIBUN2', 'ZIP_NO_OLD', 'ZIP_SN']
zipcode_path = 'random_zipcodeKR.txt'


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
        self.korean_unicode = list(range(0xAC00, 0xD7A4))

    # yml 로딩 후 function 콜하기 쉽게 반화
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

    # line-by-line 로직에서 create table 혹은 insert into와 같은 것을 만날 때 스테이트 저장
    def set_state(self, state):
        self.state = state

    # random email 리턴
    def fake_email(self):
        return '\'' + self.faker_en.email() + '\''

    # random ip 리턴
    def fake_ip(self):
        return '\'' + self.faker_en.ipv4() + '\''

    # korean name generator를 통해 random name 리턴
    def korean_name(self):
        name = ''
        for _ in range(3):
            name += chr(random.choice(self.korean_unicode))
        return '\'' + name + '\''
        # return '\'' + random.choice([namer.generate(True), namer.generate(False)]) + '\''

    # names 모듈을 통해 영어 랜덤 이름 리턴
    def english_name(self):
        return '\'' + names.get_full_name() + '\''

    # 전화번호 대쉬가 있는 경우의 랜덤 리턴
    def phone_withdash(self, front_3dgits):
        if front_3dgits.startswith('02'):
            return '\'' + '02' + "-" + str(random.randint(0, 9999)).zfill(4) + "-" + str(random.randint(0, 9999)).zfill(
                4) + '\''
        else:
            return '\'' + front_3dgits + "-" + str(random.randint(0, 9999)).zfill(4) + "-" + str(
                random.randint(0, 9999)).zfill(
                4) + '\''

    # 전화번호 대쉬가 없는 경우의 랜덤 리턴
    def phone_nodash(self, front_3dgits):
        if front_3dgits.startswith('02'):
            return '\'' + '02' + str(random.randint(0, 9999)).zfill(4) + str(random.randint(0, 9999)).zfill(
                4) + '\''
        else:
            return '\'' + front_3dgits + str(random.randint(0, 9999)).zfill(4) + str(random.randint(0, 9999)).zfill(
                4) + '\''

    # 숫자, 대소문자, 심볼, 공백을 포함한 랜덤 스트링 리턴
    def random_string(self, **params):
        string_set = ''
        if 'digit' in params['object']:
            string_set += string.digits
        if 'en_lowercase' in params['object']:
            string_set += string.ascii_lowercase
        if 'en_uppercase' in params['object']:
            string_set += string.ascii_uppercase
        if 'kr' in params['object']:
            for each in random.sample(self.korean_unicode,30):
                string_set += chr(each)
        if 'symbol' in params['object']:
            string_set += string.punctuation.replace('\'', '').replace('\\','')
            # string_set += string.punctuation.replace('\\', '')
        if 'blank' in params['object']:
            string_set += ' '
        ret = '\'' + ''.join(random.choice(string_set) for _ in range(params['length'])) + '\''
        return ret
        # if object == 'digit':
        #     ret = '\'' + ''.join(random.choice(string.digits) for _ in range(length)) + '\''
        # return ret

    # params에서 정해진 스트링 리턴
    def set_string(self, **params):
        string = '\'' + params['string'] + '\''
        return string

    # Faker를 통해 랜덤 한국 주소 리턴
    def fake_kor_address(self):
        # fake = Faker('ko-KR')
        return '\'' + self.faker_kr.address() + '\''

    # Faker를 통해 랜덤 한국 우편번호 리턴
    def fake_kor_zipcode(self):
        # fake = Faker('ko-KR')
        return '\'' + self.faker_kr.postcode() + '\''

    # Faker를 통해 랜덤 미국 주소 리턴
    def fake_eng_address(self):
        # fake = Faker()
        return '\'' + self.faker_en.address() + '\''

    # Faker를 통해 랜덤 미국 우편번호 리턴
    def fake_eng_zipcode(self):
        # fake = Faker()
        return '\'' + self.faker_en.postcode() + '\''

    # Faker를 통해 숫자, 소문자 포함 10자리 랜덤 리턴
    def fake_account(self):
        return '\'' + ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10)) + '\''

    # 출생연월 yymmdd 형태로 랜덤 리턴
    def fake_birth(self):
        start_date = datetime.date(1900, 1, 1)
        end_date = datetime.date.today()
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        yymmdd = str(random_date.year) + str(random_date.month).zfill(2) + str(random_date.day).zfill(2)
        return '\'' + yymmdd + '\''

    # nice no 10000~99999로 랜덤 리턴
    def rand_nice_no(self):
        return str(random.randint(10000, 99999))

    # 리스트 형태 lst에서 랜덤 리턴
    def rand_element(self, lst):
        return '\'' + random.choice(lst) + '\''

    # 읽어드린 address 라인에서 우편번호 리턴
    def kr_zipcode(self, address):
        return '\'' + address[adr_meta.index('ZIP_NO')] + '\''

    # 읽어드린 address 라인에서 도로명 주소(시도+시군구+도로) 리턴
    def kr_doro(self, address):
        return '\'' + address[adr_meta.index('SIDO')] + ' ' + address[adr_meta.index('SIGUNGU')] + ' ' + address[
            adr_meta.index('DORO')] + '\''

    # 읽어드린 address 라인에서 상세주소(건물이름+법정동이름) 리턴
    def kr_doro_detail(self, address):
        ret = address[adr_meta.index('BUILD_NM')] + ' ' + address[adr_meta.index('DONG_NM')] + ' ' + str(
            random.randint(1, 20)) + '층'
        return '\'' + ret.strip() + '\''

    # 규칙에 맞게 한국 랜덤 주민번호 리턴
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

    def split_insert(self, line):
        inQuotes = 0  # in Quotes=1, not in Quotes=0
        isEscape = 0  # escaped character=1, nomal character=0

        lst = []
        #array = []
        column = ''
        for a in line:
            if a == ',' and inQuotes == 0:
                lst.append(column)
                column = ''
            elif a == '\'' and inQuotes == 0 and isEscape == 0:
                column+=a
                inQuotes = 1
            elif a == '\'' and inQuotes == 1 and isEscape == 0:
                column+=a
                inQuotes = 0
            elif a == '\\':
                column+=a
                if isEscape ==1:
                    isEscape=0
                else:
                    isEscape = 1
            else:
                if isEscape == 1:
                    isEscape = 0
                column+=a
        lst.append(column)
        # print(lst)
        return lst

    # convert job in line
    def convert(self, _line, infofile, target_table, table2cols, option):
        # _line = _line[0].split(',')
        # _line = [ele for each in re.split(r',(?=\')', _line[0]) for ele in each.split(',')]
        # _line = re.split(r",(?=(?:[^\']*\'[^\']*\')*[^\']*$)", _line[0])
        # _line = re.split(r"(?:^|,)(\"(?:[^\"]+|\"\")*\"|[^,]*)", _line[0])
        # _line = re.split(r"/'[^/']*/'|[^,]+",_line[0])
        _line = self.split_insert(_line[0])
        _line_blank = _line.copy()
        for name, func, params in infofile[self.dbname][target_table]:
            # if option == 'scrambled':
            element = _line[table2cols[target_table].index(name)]
            if params is None:
                if func in ['phone_withdash', 'phone_nodash']:
                    front_3digit = element[1:4]
                    if element.lower() not in ['null'] and element.strip('\'') not in ['Removed', '']:
                        _line[table2cols[target_table].index(name)] = eval('self.' + func)(front_3digit)
                else:
                    if element.lower() not in ['null'] and element.strip('\'') not in ['Removed', '']:
                        _line[table2cols[target_table].index(name)] = eval('self.' + func)()
            elif func == 'rand_element':
                if element.lower() not in ['null'] and element.strip('\'') not in ['Removed', '']:
                    _line[table2cols[target_table].index(name)] = eval('self.' + func)(params[0]['object'])
            elif func == 'random_address':
                fullAdr = self.zipcode_kr.readline()
                if fullAdr is None:
                    self.zipcode_kr = open(zipcode_path)
                    fullAdr = self.zipcode_kr.readline()
                address = fullAdr.split('|')
                for each in params:
                    _element = _line[table2cols[target_table].index(each['column'])]
                    if _element.lower() not in ['null'] and _element.strip('\'') not in ['Removed', '']:
                        _line[table2cols[target_table].index(each['column'])] = eval('self.' + each['cvt_option'])(
                            address)
            else:
                _params = {}
                for each in params:
                    _params.update(each)
                if element.lower() not in ['null'] and element.strip('\'') not in ['Removed', '']:
                    _line[table2cols[target_table].index(name)] = eval('self.' + func)(**_params)
            # elif option == 'blank':
            _line_blank[table2cols[target_table].index(name)] = ''
        _line = '(' + ','.join(_line) + ')'
        _line_blank = '(' + ','.join(_line_blank) + ')'
        return _line,_line_blank

    # parsing via line-by-line
    def parse(self):
        table2cols = dict()
        out_scrambled = open(self.outfile_scrambled, 'w')
        out_blank = open(self.outfile_blank, 'w')
        with open(self.dumpfile) as f:
            for line in f:
                # line = line.decode('UTF-8')
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
                        _line_scrambled, _line_blank = self.convert(l, self.infofile, target_table, table2cols, option='scrambled')
                        # _line_blank = self.convert(l, self.infofile, target_table, table2cols, option='blank')
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
