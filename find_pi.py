import argparse
import re

class PIfinder:
    def __init__(self,
                 dumpfile='dump.sql'):
        self.dumpfile = dumpfile
    def find_pi(self):
        li = 0
        state = 0 # 1: in create table, 0: outside of create table
        with open(self.dumpfile) as f:
            for line in f:
                li += 1
                if re.match("CREATE TABLE `", line) is not None:
                    # Find create table
                    m = re.search("(?:\x60)(\S*)(?:\x60)", line)
                    table = m.group(1)
                    state = 1
                    print(str(li)+" - TABLE NAME: "+table)
                elif state == 1:
                    # Find column
                    if line.strip().lower().startswith('`'):
                        col = re.search('\`(\S*)\`', line)
                        com = re.search('COMMENT\s\'(.*)\'',line)
                        if col is not None and com is not None:
                            lst=[]
                            if re.search('이름|회원|명|name|NM',com.group(1)) is not None:
                                lst.append('name')
                            if re.search('휴대폰|전화|phone|연락처',com.group(1)) is not None:
                                lst.append('phone')
                            if re.search('메일|이메일|mail',com.group(1)) is not None:
                                lst.append('email')
                            if re.search('주소|도로|우편|post',com.group(1)) is not None:
                                lst.append('post')
                            if re.search('생일|birth',com.group(1)) is not None:
                                lst.append('birth')
                            if re.search('주민|res',com.group(1)) is not None:
                                lst.append('rrn')
                            if re.search('계좌|account',com.group(1)) is not None:
                                lst.append('acount')
                            if re.search('아이디|ID|id|패스워드|비밀|PW|PSWD',com.group(1)) is not None:
                                lst.append('id/pw')
                            if re.search('아이피|ip|IP',com.group(1)) is not None:
                                lst.append('ip')
                            if lst:
                                print(col.group(1)+":"com.group(1)+" - "+str(lst))
                    if line.strip().endswith(';'):
                        print("")
                        state = 0

parser = argparse.ArgumentParser(description='find personal information in sqldump file')
parser.add_argument('--sql', type=str, default=None)
args = parser.parse_args()


finder = PIfinder(dumpfile=args.sql)

finder.find_pi()