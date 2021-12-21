import random

zipcode_kr = open('../random_zipcodeKR.txt')

#우편번호|시도|시도영문|시군구|시군구영문|읍면|읍면영문|도로명코드|도로명|도로명영문|지하여부|건물번호본번|건물번호부번|건물관리번호|다량배달처명|시군구용건물명|법정동코드|법정동명|리명|행정동명|산여부|지번본번|읍면동일련번호|지번부번|구우편번호|우편번호일련번호
adr_meta=['ZIP_NO','SIDO','SIDO_ENG','SIGUNGU','SIGUNGU_ENG','EUPMYUN','EUPMYUN_ENG',
    'DORO_CD','DORO','DORO_ENG','UNDERGROUNT_YN','BUILD_NO1','BUILD_NO2',"BUILD_NO_MANAGE_NO",
    'DARYANG_NM','BUILD_NM','DONG_CD','DONG_NM','RI','H_DONG_NM','SAN_YN','ZIBUN1',
    'EUPMYUN_DONG_SN','ZIBUN2','ZIP_NO_OLD','ZIP_SN']


def korean_address():
    fullAdr=zipcode_kr.readline()
    address=fullAdr.split('|')
    zipcode=address[adr_meta.index('ZIP_NO')]
    mainAdr=address[adr_meta.index('SIDO')]+' '+address[adr_meta.index('SIGUNGU')]+' '+address[adr_meta.index('DORO')]
    #print(zipcode)
    #print(mainAdr)

for i in range(1,10000):
    korean_address()

