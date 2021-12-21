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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 STATS_PERSISTENT=0 COMMENT='sample_table';


LOCK TABLES `sample_table1` WRITE;

INSERT INTO `sample_table1` VALUES
(0,'전기연','010-1234-1114','kyjeon@ibm.com','서울특별시 도봉구 테헤란로 민지안최동(땡땡아파트)','13123','880218-101010'),
(1,'이승연','010-3452-2322','sylee@ibm.com','인천광역시 도봉구 언주341로 정웅이최마을','14852','950118-201618'),
(2,'공진기','010-2342-1334','jkkong@ibm.com','경상북도 괴산군 서초대길','69117','811218-175110'),
(3,'김현태','010-2222-2344','htkim@ibm.com','서울특별시 마포구 서초중앙로 예진김면','54904','840928-134530')
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
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 STATS_PERSISTENT=0 COMMENT='sample_table';


LOCK TABLES `sample_table2` WRITE;

INSERT INTO `sample_table2` VALUES
(0,'전기현','010-1234-1114','kyjeon@ibm.com','서울특별시 도봉구 테헤란로 민지안최동 (벽산아파트)','13123','880218-101010'),
(1,'이승현','010-3452-2322','sylee@ibm.com','인천광역시 도봉구 언주341로 정웅이최마을','14852','950118-201618'),
(2,'김진기','010-2342-1334','jkkong@ibm.com','경상북도 괴산군 서초대길','69117','811218-175110'),
(3,'김현수','010-2222-2344','htkim@ibm.com','서울특별시 마포구 서초중앙로 예진김면','54904','840928-134530');
/*!40000 ALTER TABLE `sample_table` ENABLE KEYS */;
UNLOCK TABLES;
