-- MySQL dump 10.13  Distrib 5.7.23, for Linux (x86_64)
--
-- Host: localhost    Database: MOSHOU
-- ------------------------------------------------------
-- Server version	5.7.23-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `MOSHOU`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `MOSHOU` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `MOSHOU`;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) DEFAULT NULL,
  `article_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (1,10000,10000),(2,10001,10001),(3,10002,10000),(4,10003,10015),(5,10004,10006),(6,10025,10006),(7,10009,10000);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hero`
--

DROP TABLE IF EXISTS `hero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hero` (
  `id` int(11) DEFAULT NULL,
  `name` char(15) DEFAULT NULL,
  `sex` enum('男','女') DEFAULT NULL,
  `country` char(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hero`
--

LOCK TABLES `hero` WRITE;
/*!40000 ALTER TABLE `hero` DISABLE KEYS */;
INSERT INTO `hero` VALUES (1,'曹操','男','魏国'),(2,'小乔','女','吴国'),(3,'诸葛亮','男','蜀国'),(4,'貂蝉','女','东汉'),(5,'赵子龙','男','蜀国'),(6,'魏延','男','蜀国');
/*!40000 ALTER TABLE `hero` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo`
--

DROP TABLE IF EXISTS `sanguo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sanguo` (
  `id` int(11) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `gongji` int(11) DEFAULT NULL,
  `fangyu` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('男','女') DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo`
--

LOCK TABLES `sanguo` WRITE;
/*!40000 ALTER TABLE `sanguo` DISABLE KEYS */;
INSERT INTO `sanguo` VALUES (1,'诸葛亮',120,20,'男','蜀国'),(2,'司马懿',119,25,'男','魏国'),(3,'关羽',188,60,'男','蜀国'),(4,'赵子龙',360,88,'男','蜀国'),(5,'孙权',100,60,'男','吴国'),(6,'貂蝉',666,10,'女','魏国'),(7,NULL,1000,99,'男','蜀国'),(8,'',1005,88,'女','蜀国');
/*!40000 ALTER TABLE `sanguo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo2`
--

DROP TABLE IF EXISTS `sanguo2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sanguo2` (
  `id` int(11) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `gongji` int(11) DEFAULT NULL,
  `fangyu` tinyint(3) unsigned DEFAULT NULL,
  `sex` enum('男','女') DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo2`
--

LOCK TABLES `sanguo2` WRITE;
/*!40000 ALTER TABLE `sanguo2` DISABLE KEYS */;
INSERT INTO `sanguo2` VALUES (1,'诸葛亮',120,20,'男','蜀国'),(2,'司马懿',119,25,'男','魏国'),(3,'关羽',188,60,'男','蜀国'),(4,'赵子龙',360,88,'男','蜀国'),(5,'孙权',100,60,'男','吴国'),(6,'貂蝉',666,10,'女','魏国'),(7,NULL,1000,99,'男','蜀国'),(8,'',1005,88,'女','蜀国');
/*!40000 ALTER TABLE `sanguo2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo3`
--

DROP TABLE IF EXISTS `sanguo3`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sanguo3` (
  `id` int(11) DEFAULT NULL,
  `name` char(20) DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo3`
--

LOCK TABLES `sanguo3` WRITE;
/*!40000 ALTER TABLE `sanguo3` DISABLE KEYS */;
INSERT INTO `sanguo3` VALUES (1,'诸葛亮','蜀国'),(2,'司马懿','魏国'),(3,'关羽','蜀国'),(4,'赵子龙','蜀国'),(5,'孙权','吴国'),(6,'貂蝉','魏国'),(7,NULL,'蜀国'),(8,'','蜀国');
/*!40000 ALTER TABLE `sanguo3` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sanguo4`
--

DROP TABLE IF EXISTS `sanguo4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sanguo4` (
  `name` char(20) DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sanguo4`
--

LOCK TABLES `sanguo4` WRITE;
/*!40000 ALTER TABLE `sanguo4` DISABLE KEYS */;
INSERT INTO `sanguo4` VALUES ('孙权','吴国'),('貂蝉','魏国');
/*!40000 ALTER TABLE `sanguo4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Current Database: `db4`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `db4` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `db4`;

--
-- Table structure for table `bjtab`
--

DROP TABLE IF EXISTS `bjtab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `bjtab` (
  `stu_id` int(11) DEFAULT NULL,
  `name` varchar(20) DEFAULT NULL,
  `money` smallint(6) DEFAULT NULL,
  KEY `stu_id` (`stu_id`),
  CONSTRAINT `bjtab_ibfk_1` FOREIGN KEY (`stu_id`) REFERENCES `jftab` (`id`) ON DELETE SET NULL ON UPDATE SET NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bjtab`
--

LOCK TABLES `bjtab` WRITE;
/*!40000 ALTER TABLE `bjtab` DISABLE KEYS */;
INSERT INTO `bjtab` VALUES (8,'点秋香',300);
/*!40000 ALTER TABLE `bjtab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `city`
--

DROP TABLE IF EXISTS `city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `c_id` int(11) DEFAULT NULL,
  `c_name` varchar(15) DEFAULT NULL,
  `cfather_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `city`
--

LOCK TABLES `city` WRITE;
/*!40000 ALTER TABLE `city` DISABLE KEYS */;
INSERT INTO `city` VALUES (1,131100,'石家庄市',130000),(2,131101,'沧州市',130000),(3,131102,'廊坊市',130000),(4,131103,'西安市',140000),(5,131104,'成都市',150000),(6,131105,'重庆市',150000),(7,131106,'广州市',160000),(8,131107,'济南市',170000),(9,131108,'武汉市',180000),(10,131109,'郑州市',190000),(11,131110,'北京市',320000),(12,131111,'天津市',320000),(13,131112,'上海市',320000),(14,131113,'哈尔滨',320001),(15,131114,'雄安新区',320002);
/*!40000 ALTER TABLE `city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `c_id` int(11) NOT NULL,
  `c_name` varchar(20) DEFAULT NULL,
  `c_age` tinyint(3) unsigned DEFAULT NULL,
  `c_sex` set('M','F') DEFAULT NULL,
  `c_city` varchar(20) DEFAULT NULL,
  `c_salary` decimal(12,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Zhangsan',25,'M','Beijing',9200.00),(2,'Lisi',30,'F','Shanghai',11500.00),(3,'Wangwu',27,'M','Shenzhen',3450.00);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jftab`
--

DROP TABLE IF EXISTS `jftab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jftab` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `class` char(5) DEFAULT NULL,
  `money` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jftab`
--

LOCK TABLES `jftab` WRITE;
/*!40000 ALTER TABLE `jftab` DISABLE KEYS */;
INSERT INTO `jftab` VALUES (3,'文征明','AID07',300),(8,'点秋香','AID07',300);
/*!40000 ALTER TABLE `jftab` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `o_id` int(11) DEFAULT NULL,
  `o_name` varchar(30) DEFAULT NULL,
  `o_price` decimal(10,2) DEFAULT NULL,
  KEY `o_id` (`o_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,'iphone',5288.00),(1,'ipad',3299.00),(3,'mate9',3688.00),(2,'iwatch',2222.00),(2,'r11',4400.00);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sheng`
--

DROP TABLE IF EXISTS `sheng`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sheng` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `s_id` int(11) DEFAULT NULL,
  `s_name` varchar(15) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sheng`
--

LOCK TABLES `sheng` WRITE;
/*!40000 ALTER TABLE `sheng` DISABLE KEYS */;
INSERT INTO `sheng` VALUES (1,130000,'浙江省'),(2,140000,'陕西省'),(3,150000,'四川省'),(4,160000,'广东省'),(5,170000,'山东省'),(6,180000,'湖北省'),(7,190000,'河南省'),(9,200001,'云南省'),(10,200002,'山西省'),(11,230000,'安徽省'),(36,500000,'广西省');
/*!40000 ALTER TABLE `sheng` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t4`
--

DROP TABLE IF EXISTS `t4`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t4` (
  `id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t4`
--

LOCK TABLES `t4` WRITE;
/*!40000 ALTER TABLE `t4` DISABLE KEYS */;
/*!40000 ALTER TABLE `t4` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `t888`
--

DROP TABLE IF EXISTS `t888`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `t888` (
  `id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `t888`
--

LOCK TABLES `t888` WRITE;
/*!40000 ALTER TABLE `t888` DISABLE KEYS */;
/*!40000 ALTER TABLE `t888` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `username` varchar(20) DEFAULT NULL,
  `password` char(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('Tom','7c4a8d09ca3762af61e59520943dc26494f8941b');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `xian`
--

DROP TABLE IF EXISTS `xian`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `xian` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `x_id` int(11) DEFAULT NULL,
  `x_name` varchar(15) DEFAULT NULL,
  `xfather_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `xian`
--

LOCK TABLES `xian` WRITE;
/*!40000 ALTER TABLE `xian` DISABLE KEYS */;
INSERT INTO `xian` VALUES (1,132100,'正定县',131100),(2,132102,'浦东新区',131112),(3,132103,'武昌区',131108),(4,132104,'哈哈',131115),(5,132105,'安新县',131114),(6,132106,'容城县',131114),(7,132107,'雄县',131114),(8,132108,'嘎嘎',131115);
/*!40000 ALTER TABLE `xian` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-04 18:50:23
