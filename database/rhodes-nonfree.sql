-- MySQL dump 10.16  Distrib 10.1.37-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: rhodes
-- ------------------------------------------------------
-- Server version	10.1.37-MariaDB-3

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `rhodes`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `rhodes` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;

USE `rhodes`;

--
-- Table structure for table `cables`
--

DROP TABLE IF EXISTS `cables`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cables` (
  `ID` int(11) NOT NULL,
  `UPC` varchar(50) DEFAULT NULL,
  `Connector_A` varchar(50) DEFAULT NULL,
  `Connector_B` varchar(50) DEFAULT NULL,
  `Length` varchar(50) DEFAULT NULL,
  `In_Stock` int(11) DEFAULT NULL,
  `Taken` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `cables_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `equipment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `comments`
--

DROP TABLE IF EXISTS `comments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comments` (
  `ID` int(200) NOT NULL,
  `Thread` int(150) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Author` int(11) DEFAULT NULL,
  `Content` varchar(5000) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `computers`
--

DROP TABLE IF EXISTS `computers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `computers` (
  `ID` int(11) NOT NULL,
  `Manufacturer_Brand` varchar(50) DEFAULT NULL,
  `BIOS_Version` varchar(50) DEFAULT NULL,
  `Service_Tag` varchar(50) DEFAULT NULL,
  `Asset_Tag` varchar(50) DEFAULT NULL,
  `Ownership_Tag` varchar(50) DEFAULT NULL,
  `Manufacture_Date` timestamp NULL DEFAULT NULL,
  `Ownership_Date` timestamp NULL DEFAULT NULL,
  `Express_Service_Code` varchar(50) DEFAULT NULL,
  `Signed_Firmware_Update_Enabled` tinyint(1) DEFAULT NULL,
  `Memory_Installed_Amount` varchar(50) DEFAULT NULL,
  `Memory_Available` varchar(50) DEFAULT NULL,
  `Memory_Speed` varchar(50) DEFAULT NULL,
  `Memory_Channel_Mode` varchar(50) DEFAULT NULL,
  `Memory_Technology` varchar(50) DEFAULT NULL,
  `DIMM_A_Size` varchar(50) DEFAULT NULL,
  `DIMM_B_Size` varchar(50) DEFAULT NULL,
  `DIMM_C_Size` varchar(50) DEFAULT NULL,
  `DIMM_D_Size` varchar(50) DEFAULT NULL,
  `DIMM_E_Size` varchar(50) DEFAULT NULL,
  `DIMM_F_Size` varchar(50) DEFAULT NULL,
  `Processor_Type` varchar(50) DEFAULT NULL,
  `Core_Count` smallint(6) DEFAULT NULL,
  `Processor_ID` varchar(50) DEFAULT NULL,
  `Current_Clock_Speed` varchar(50) DEFAULT NULL,
  `Min_Clock_Speed` varchar(50) DEFAULT NULL,
  `Max_Clock_Speed` varchar(50) DEFAULT NULL,
  `Processor_L1_Cache` varchar(50) DEFAULT NULL,
  `Processor_L2_Cache` varchar(50) DEFAULT NULL,
  `Processor_L3_Cache` varchar(50) DEFAULT NULL,
  `Processor_L4_Cache` varchar(50) DEFAULT NULL,
  `HyperThread_Capable` tinyint(1) DEFAULT NULL,
  `64_Bit` tinyint(1) DEFAULT NULL,
  `32_Bit` tinyint(1) DEFAULT NULL,
  `Hard_Drive_ID` varchar(50) DEFAULT NULL,
  `Hard_Drive_Space` varchar(50) DEFAULT NULL,
  `Solid_State_Drive_ID` varchar(50) DEFAULT NULL,
  `Solid_State_Drive_Space` varchar(50) DEFAULT NULL,
  `M2_PCIe_SDD_ID` varchar(50) DEFAULT NULL,
  `M2_PCIe_SDD_Space` varchar(50) DEFAULT NULL,
  `Video_Controller` varchar(50) DEFAULT NULL,
  `Video_BIOS_Version` varchar(50) DEFAULT NULL,
  `Video_Memory` varchar(50) DEFAULT NULL,
  `Panel_Type` varchar(50) DEFAULT NULL,
  `Native_Resolution` varchar(50) DEFAULT NULL,
  `Audio_Controller` varchar(50) DEFAULT NULL,
  `Wifi_Brand` varchar(50) DEFAULT NULL,
  `AudioJack` tinyint(1) DEFAULT NULL,
  `Wifi` tinyint(1) DEFAULT NULL,
  `BlueTooth` tinyint(1) DEFAULT NULL,
  `RJ45` tinyint(1) DEFAULT NULL,
  `RJ11` tinyint(1) DEFAULT NULL,
  `HDMI` tinyint(1) DEFAULT NULL,
  `VGA` tinyint(1) DEFAULT NULL,
  `DVI` tinyint(1) DEFAULT NULL,
  `DisplayPort` tinyint(1) DEFAULT NULL,
  `MiniDisplayPort` tinyint(1) DEFAULT NULL,
  `USBA2` tinyint(1) DEFAULT NULL,
  `USBA3` tinyint(1) DEFAULT NULL,
  `USBC` tinyint(1) DEFAULT NULL,
  `Serial_Port` tinyint(1) DEFAULT NULL,
  `Parallel_Port` tinyint(1) DEFAULT NULL,
  `Is_Laptop` tinyint(1) DEFAULT NULL,
  `Legacy_Boot_Enabled` tinyint(1) DEFAULT NULL,
  `UEFI_Boot_Enabled` tinyint(1) DEFAULT NULL,
  `Secure_Boot_Enabled` tinyint(1) DEFAULT NULL,
  `Legacy_Option_ROMs_Enabled` tinyint(1) DEFAULT NULL,
  `Attempt_Legacy_Boot_Enabled` tinyint(1) DEFAULT NULL,
  `UEFI_Network_Stack_Enabled` tinyint(1) DEFAULT NULL,
  `Operating_System` varchar(15) DEFAULT NULL,
  `OS_Version` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `computers_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `equipment` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employees` (
  `ID` int(11) NOT NULL,
  `Position` varchar(100) NOT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`ID`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `equipment`
--

DROP TABLE IF EXISTS `equipment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipment` (
  `ID` int(100) NOT NULL,
  `Name` varchar(100) DEFAULT NULL,
  `Type` varchar(50) DEFAULT NULL,
  `Model_ID` varchar(50) DEFAULT NULL,
  `Serial_Num` varchar(50) DEFAULT NULL,
  `Owner_ID` int(11) NOT NULL,
  `Price` int(11) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Owner_ID` (`Owner_ID`),
  CONSTRAINT `equipment_ibfk_1` FOREIGN KEY (`Owner_ID`) REFERENCES `people` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `ID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Location` varchar(200) NOT NULL,
  `Email` varchar(100) DEFAULT NULL,
  `Phone` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tickets`
--

DROP TABLE IF EXISTS `tickets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tickets` (
  `ID` int(150) NOT NULL,
  `Created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `Due` timestamp NULL DEFAULT NULL,
  `Category` varchar(150) DEFAULT NULL,
  `Title` varchar(150) DEFAULT NULL,
  `Responder` int(11) DEFAULT NULL,
  `Requester` int(11) DEFAULT NULL,
  `Elevation` varchar(150) DEFAULT NULL,
  `Status` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  KEY `Responder` (`Responder`),
  KEY `Requester` (`Requester`),
  CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`Responder`) REFERENCES `people` (`ID`),
  CONSTRAINT `tickets_ibfk_2` FOREIGN KEY (`Requester`) REFERENCES `people` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-24 11:28:47
