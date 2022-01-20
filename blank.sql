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
(NULL,,,,,13112,'(PRD) 비회원 \"엄응진\" 특수~!@#$%^&*(),_+|\\[]{};:\'\"./<>?문자',),
(1,,,,,'14852','950118-201618',),
(2,,,,,'69117','811218-175110',),
(3,,,,,'54904','840928-134530',)
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
(0,,,'kyjeon@ibm.com',,'13123',,),
(1,,,'sylee@ibm.com',,'14852',,),
(2,,,'jkkong@ibm.com',,'69117',,),
(3,,,'htkim@ibm.com',,'54904',,);
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
(0,,,'kyjeon@ibm.com',,,,,'19880218',,,,,,,),
(1,,,'sylee@ibm.com',,,,,'19950118',,,,,,,),
(2,,,'',,,,, '19811218',,,,,,,),
(3,,,'htkim@ibm.com',,,,, '19840928',,,,,,,);
/*!40000 ALTER TABLE `sample_table` ENABLE KEYS */;
UNLOCK TABLES;