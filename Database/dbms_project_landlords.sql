CREATE DATABASE  IF NOT EXISTS `dbms_project` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `dbms_project`;
-- MySQL dump 10.13  Distrib 8.0.11, for Win64 (x86_64)
--
-- Host: localhost    Database: dbms_project
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `landlords`
--

DROP TABLE IF EXISTS `landlords`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `landlords` (
  `email_id` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `middle_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `contact_number` varchar(10) DEFAULT NULL,
  `address` varchar(100) NOT NULL,
  `landlord_id` varchar(100) NOT NULL,
  PRIMARY KEY (`landlord_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `landlords`
--

LOCK TABLES `landlords` WRITE;
/*!40000 ALTER TABLE `landlords` DISABLE KEYS */;
INSERT INTO `landlords` VALUES ('Joseph@mailtor.com','Joseph123','Joseph','Carlos','Marshall','7528228675','10039 Jenna Canyon, Hyderabad, Telangana, 504995','1419190420'),('Nicole@yahoo.com','Nicole123','Nicole','Rosemary','Lovig','7883239889','09323 Adams Pass Apt. 220, Bangalore, Karnataka, 564825','1424898048'),('Michelle@gmail.com','Michelle123','Michelle','','Obrien','8909374965','0319 Perry Prairie, Kochi, Kerala, 686285','1849409719'),('Wade@yahoo.com','Wade123','Wade','Judy','Perretta','9746873036','704 Annette Springs, Chennai, Tamil Nadu, 600126','1855197282'),('Lester@gmail.com','Lester123','Lester','','Killoren','8184700915','3927 Megan Key Apt. 950, Kochi, Kerala, 689948','1990602977'),('Karen@mailtor.com','Karen123','Karen','','Miles','7516234965','266 Lauren Lodge Apt. 460, Mumbai, Maharashtra, 400263','2001610088'),('Mary@gmail.com','Mary123','Mary','','Cook','8281583047','2398 Angela Courts, Allahabad, Uttar Pradesh, 216769','2347060178'),('Dolores@yahoo.com','Dolores123','Dolores','','Grennan','9712200011','4028 Nancy Estate, Mumbai, Maharashtra, 400854','2385097151'),('Carolyn@gmail.com','Carolyn123','Carolyn','','Brooks','9865352642','506 Thompson Crossing Apt. 107, Chennai, Tamil Nadu, 600919','2531558835'),('Darlene@mailtor.com','Darlene123','Darlene','','Mason','9420133409','098 Richard Lodge, Mumbai, Maharashtra, 400638','2587455676'),('Debra@yahoo.com','Debra123','Debra','','Hamilton','7454326091','086 Allison Springs, Allahabad, Uttar Pradesh, 219775','2680562405'),('George@yahoo.com','George123','George','','Witte','7754670054','4149 Young Flat, Bangalore, Karnataka, 568484','2912318101'),('Danny@mailtor.com','Danny123','Danny','','Webb','8911209423','587 Robert Plaza Apt. 008, Hyderabad, Telangana, 501071','2929580744'),('Christine@mailtor.com','Christine123','Christine','','Nieves','7152528565','430 Casey Fort Suite 345, Hyderabad, Telangana, 502670','3022311394'),('Gail@mailtor.com','Gail123','Gail','','Hughes','7591639917','6046 Joseph Hill, Bangalore, Karnataka, 564213','3032164049'),('Randy@mailtor.com','Randy123','Randy','Ann','Johnston','7769868681','9784 Coleman Prairie, Bhopal, Madhya Pradesh, 462226','3224489412'),('Samuel@gmail.com','Samuel123','Samuel','','Bordner','7520163720','433 Jeremy Views Suite 909, Delhi, 118494','3547534097'),('Andy@gmail.com','Andy123','Andy','','Green','9636244638','11928 Burns Circle, Chennai, Tamil Nadu, 600881','354821128'),('Judy@gmail.com','Judy123','Judy','George','Hamelin','9692879429','402 Heather Turnpike, Bhopal, Madhya Pradesh, 462727','3798556057'),('Suzanne@mailtor.com','Suzanne123','Suzanne','','Boulos','7883337801','68692 Wong Square Suite 680, Bhopal, Madhya Pradesh, 462691','3809187200'),('Jacqueline@yahoo.com','Jacqueline123','Jacqueline','','Gray','8795221656','07766 Graves Lodge, Kochi, Kerala, 688846','3812227101'),('Glenn@gmail.com','Glenn123','Glenn','Reginald','Robinson','7643658965','0717 Mcdonald Motorway, Bangalore, Karnataka, 562851','3834886282'),('landysmith@gmail.com','mohit123','Land','Lord','Smith','9035230091','askj','3892593249'),('Leigh@mailtor.com','Leigh123','Leigh','Lisa','Parrish','7639680261','USCGC Wilson, Chennai, Tamil Nadu, 600249','3965166562'),('Maurice@yahoo.com','Maurice123','Maurice','','Mcmillin','9616306534','4999 Dean Plaza Apt. 127, Delhi, 11256','4009495065'),('Jessica@mailtor.com','Jessica123','Jessica','Joel','Arteaga','836754427','6361 Wagner Dam, Mumbai, Maharashtra, 400908','4036818408'),('William@gmail.com','William123','William','','Carsey','8165918467','7357 Scott Gardens, Chennai, Tamil Nadu, 600489','4156385700'),('Bradford@gmail.com','Bradford123','Bradford','','Miller','8549072956','Unit 9824 Box 2978, Chennai, Tamil Nadu, 600266','570686234'),('Donald@mailtor.com','Donald123','Donald','','Holland','7135549072','3840 James Squares, Kochi, Kerala, 688951','878415387'),('Jesse@gmail.com','Jesse123','Jesse','Quentin','Snyder','7580788907','90144 Hill Extension, Allahabad, Uttar Pradesh, 212255','950739919'),('Lauren@mailtor.com','Lauren123','Lauren','Lydia','Gonzalez','8886551843','305 Jessica Well, Bangalore, Karnataka, 566467','958374477');
/*!40000 ALTER TABLE `landlords` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-24 19:17:02
