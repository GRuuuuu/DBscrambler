import re;
import yaml;

textArr = ["배달시 인천시 서구 청마로 당하동 123동 456호 앞으로 배달해주세요", 
        "안녕하세요 제 이름은 홍길동입니다링딩동 메일주소 sngylee@kr.ibm.com으로 연락주세요",
        "빠른 배송 부탁드립니다",
        "연락은 01012345670으로 부탁",
        "010-1234-2345입니다.",
        "나의 주민번호는 111111-2222222",
        "경비실에 맡겨주세요 ."]

def isTel(text):
    if re.search('[0-9]{2,3}-[0-9]{4}-[0-9]{4}',text) is not None:
        return True;
    elif re.search('[0-9]{2,3}[0-9]{8}',text) is not None:
        return True;
    else:
        return False;

def isAdr(text):
    if re.search('[0-9]{3,4}동',text) is not None:
        return True;
    elif re.search('[0-9]{3,4}호',text) is not None:
        return True;
    else:
        return False;

def isEmail(text):
    if re.search('[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+[.]?\w{2,3}',text) is not None:
        return True;
    else: 
        return False;

def isRRN(text):
    if re.search('[0-9]{6}\s?-?[0-9]{7}',text) is not None:
        return True;
    else:
        return False;

def validText(text):
    if isTel(text):
        return "TEL";
    elif isAdr(text):
        return "ADDRESS";
    elif isEmail(text):
        return "EMAIL";
    elif isRRN(text):
        return "RRN";
    else:
        return None;



for text in textArr:
    res=validText(text);
    if res is not None:
        print("\""+text+"\""+"may contain personal information("+res+")");

"""
yamlFile='';
with open("./parsed_meta.yaml") as f:
    yamlFile=yaml.load(f,Loader=yaml.FullLoader);


numArr = 
"""

