-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: localhost    Database: my_data
-- ------------------------------------------------------
-- Server version	8.0.28

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `register`
--

DROP TABLE IF EXISTS `register`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `register` (
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `contact` int NOT NULL,
  `email` varchar(45) NOT NULL,
  `securityQ` varchar(45) DEFAULT NULL,
  `securityA` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `register`
--

LOCK TABLES `register` WRITE;
/*!40000 ALTER TABLE `register` DISABLE KEYS */;
INSERT INTO `register` VALUES ('anu','sidhu',221832,'anu@gmail.com','Your Pet Name','kuta',''),('biba','shrma',66676776,'bb@gmail.com','Your Pet Name','noni','vb'),('qq','vv',221453,'bh@gmail.com','Your birth place','pthankot','56'),('hlo','',78788787,'bn@gmail.com','Your birth place','moga','78'),('gh','nm',767676767,'fg@gmail.com','Your Pet Name','dogi','nbn'),('maani','',78654567,'hj@gmail.com','Your Best Fiend Name','mona','hjh'),('honey','singh',564567893,'hs@gmail.com','Your Best Fiend Name','money','hs'),('jas','kaur',56686543,'js@gmail.com','Your birth place','chd','gh'),('kapil','gh',88768767,'kapu','Your birth place','ludh','hjghjgjh'),('maan','saab',678987654,'mn@gmail.com','Your Best Fiend Name','barbie','67'),('dadi','sadi',678654321,'sd@gmail.com','Your Pet Name','dogi','67'),('v','sharma',221832,'vb@gmail.com','Your birth place','chd','nona');
/*!40000 ALTER TABLE `register` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-06-01  8:49:23
