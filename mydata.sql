-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 13, 2022 at 04:11 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mydata`
--

-- --------------------------------------------------------

--
-- Table structure for table `hospital`
--

CREATE TABLE `hospital` (
  `name` varchar(30) NOT NULL,
  `ref` varchar(35) NOT NULL,
  `dose` int(30) NOT NULL,
  `tablets` varchar(20) NOT NULL,
  `lot` varchar(40) NOT NULL,
  `issue` varchar(20) NOT NULL,
  `expiry` varchar(20) NOT NULL,
  `side_effect` varchar(30) NOT NULL,
  `bp` varchar(30) NOT NULL,
  `storage` varchar(30) NOT NULL,
  `pid` varchar(30) NOT NULL,
  `dob` varchar(20) NOT NULL,
  `pname` varchar(30) NOT NULL,
  `address` varchar(30) NOT NULL,
  `suggestion` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
