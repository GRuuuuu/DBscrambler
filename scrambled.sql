USE `mysql`
DROP TABLE IF EXISTS `sample_table0`;
CREATE TABLE `sample_table0` (
  `id` smallint(5) unsigned NOT NULL,
  `name` char(64) NOT NULL,
  `phone` char(20) NOT NULL,
  `email` char(30) NOT NULL,
  `address` char(30) NOT NULL,
  `postal` char(20) NOT NULL,
  `rid` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 STATS_PERSISTENT=0 COMMENT='sample_table';


LOCK TABLES `sample_table0` WRITE;

INSERT INTO `sample_table0` VALUES
(0,'전기','010-1234-1114','kyjeon@ibm.com','서울특별시 도봉구 테헤란로 민지안최동(벽산)','13123','880218-101010'),
(1,'이연','010-3452-2322','sylee@ibm.com','인천광역시 도봉구 언주341로 정웅이최마을','14852','950118-201618'), 
(2,'공진','010-2342-1334','jkkong@ibm.com','경상북도 괴산군 서초대길','69117','811218-175110'), 
(3,'김태','010-2222-2344','htkim@ibm.com','서울특별시 마포구 서초중앙로 예진김면','54904','840928-134530')
/*!40000 ALTER TABLE `sample_table` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `sample_table1`;
CREATE TABLE `sample_table1` (
  `id` smallint(5) unsigned NOT NULL,
  `name` char(64) NOT NULL,
  `phone` char(20) NOT NULL,
  `email` char(30) NOT NULL,
  `address` char(30) NOT NULL,
  `postal` char(20) NOT NULL,
  `rid` char(20) NOT NULL,
  `ip` char(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 STATS_PERSISTENT=0 COMMENT='sample_table';


LOCK TABLES `sample_table1` WRITE;

INSERT INTO `sample_table1` VALUES
(NULL,'읮멝뤞',NULL,NULL,'인천광역시 영등포구 반포대3거리 (수진박읍)',13112,'(PRD) 비회원 \"엄응진\" 특수~!@#$%^&*(),_+|\\[]{};:\'\"./<>?문자','12.167.17.44'),
(1,'슠뒧뜃','01046463088','RNOLYpgwzHfKv@gmail.com','인천광역시 중구 백제고분길','14852','950118-2016148','160.63.254.145'),
(2,'싊뿬욫','01051656070','SjQDJsOqeZhNK@gmail.com','제주특별자치도 청주시 청원구 잠실길','69117','811218-1754110','9.20.36.176'),
(3,'츉륝멐','01018168237','SnTCzLQFPeGRw@naver.com','강원도 수원시 권선구 강남대9로','54904','840928-1345430','161.210.193.169')
/*!40000 ALTER TABLE `sample_table` ENABLE KEYS */;
UNLOCK TABLES;

DROP TABLE IF EXISTS `sample_table2`;
CREATE TABLE `sample_table2` (
  `id` smallint(5) unsigned NOT NULL,
  `name` char(64) NOT NULL,
  `phone` char(20) NOT NULL,
  `email` char(30) NOT NULL,
  `address` char(30) NOT NULL,
  `postal` char(20) NOT NULL,
  `rid` char(20) NOT NULL,
  `birth` char(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 STATS_PERSISTENT=0 COMMENT='sample_table';


LOCK TABLES `sample_table2` WRITE;

INSERT INTO `sample_table2` VALUES
(0,'끵텓꾣','010-9851-8901','kyjeon@ibm.com','경상남도 충주시 양재천53길','13123','620803-4925381','20210214'),
(1,'빙슙펴','010-0915-1779','sylee@ibm.com','경상남도 용인시 수지구 선릉길','14852','970129-2950388','19390908'),
(2,'냊윚벑','010-1277-1681','jkkong@ibm.com','전라남도 안산시 논현로','69117','110306-3852983','20151020'),
(3,'쁶뻷웘','010-8074-7964','htkim@ibm.com','울산광역시 영등포구 잠실4거리 (지은장박리)','54904','530418-1581594','20050113');
/*!40000 ALTER TABLE `sample_table` ENABLE KEYS */;
UNLOCK TABLES;


DROP TABLE IF EXISTS `sample_table3`;
CREATE TABLE `sample_table3` (
  `id` smallint(5) unsigned NOT NULL,
  `name` char(64) NOT NULL,
  `phone` char(20) NOT NULL,
  `email` char(30) NOT NULL,
  `main_address` char(30) NOT NULL,
  `main_dtl_address` char(30) NOT NULL,
  `zipcode` char(20) NOT NULL,
  `rid` char(20) NOT NULL,
  `birth` char(10) NOT NULL,
  `account` char(20) NOT NULL,
  `member` char(20) NOT NULL,
  `emp` char(10) NOT NULL,
  `memo` char(50) NOT NULL,
  `nice_no` smallint(10) unsigned NOT NULL,
  `gd` char(5) NOT NULL,
  `ntn` char(5) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 STATS_PERSISTENT=0 COMMENT='sample_table3';


LOCK TABLES `sample_table3` WRITE;

INSERT INTO `sample_table3` VALUES
(0,'Removed','0252475443','kyjeon@ibm.com','서울특별시 용산구 한남대로42길','한남동 17층','04417','911221-2888213','19880218','gzy6g2l8gi','j6$knt꿴쑫=9$t"b','9121','S2bDzun9lauk+JzbEvydLKphVi/l1Jq3QaLokfcHBTvV/AmjCJanpKRPXLfnQ52JjMz/xlsycS5D5spZGv0Sw==',1357741591,NULL,'0'),
(1,'큨췦쀝',NULL,'sylee@ibm.com','울산광역시 울주군 화창4길','10층','44986','090526-1192738','19950118','ymxbnbo98e','a줯#쫑b~lo#떲e@"z','3359','S2bDzun9lauk+JzbEvydLKphVi/l1Jq3QaLokfcHBTvV/AmjCJanpKRPXLfnQ52JjMz/xlsycS5D5spZGv0Sw==',1083793884,'0','1'),
(2,'큙밃퀀','01072830067','','경기도 용인시 처인구 백옥대로624번길','17층','17128','960731-2212869', '19811218','efj9xg9cz4','c씎짞밒)8찴e퐺$뢀t{&','8369','S2bDzun9lauk+JzbEvydLKphVi/l1Jq3QaLokfcHBTvV/AmjCJanpKRPXLfnQ52JjMz/xlsycS5D5spZGv0Sw==',2094430538,'0','1'),
(3,'놂똙찆','01085268453','htkim@ibm.com',NULL,'1층','44961','491123-4592516', '19840928','1axefwsp3m','펻m@tp[st틨<떊;{c','3795','S2bDzun9lauk+JzbEvydLKphVi/l1Jq3QaLokfcHBTvV/AmjCJanpKRPXLfnQ52JjMz/xlsycS5D5spZGv0Sw==',842281528,'0','1');
/*!40000 ALTER TABLE `sample_table` ENABLE KEYS */;
UNLOCK TABLES;