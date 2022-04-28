-- phpMyAdmin SQL Dump
-- version 5.1.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 28, 2022 at 10:10 AM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aerolinea`
--

-- --------------------------------------------------------

--
-- Table structure for table `adminuser`
--

CREATE TABLE `adminuser` (
  `idUser` int(11) NOT NULL,
  `user` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `password` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `adminuser`
--

INSERT INTO `adminuser` (`idUser`, `user`, `password`, `nombre`) VALUES
(1, 'bernal', 'asd', 'Carlos Ramirez');

-- --------------------------------------------------------

--
-- Table structure for table `reservacion`
--

CREATE TABLE `reservacion` (
  `IDReservacion` int(10) NOT NULL,
  `Nombre` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `Correo` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `Telefono` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `fechaReservacion` varchar(255) COLLATE utf8_spanish_ci NOT NULL DEFAULT current_timestamp(),
  `NTarjeta` varchar(19) COLLATE utf8_spanish_ci NOT NULL,
  `Fecha` varchar(5) COLLATE utf8_spanish_ci NOT NULL,
  `CVV` varchar(3) COLLATE utf8_spanish_ci NOT NULL,
  `IDVuelo` int(10) NOT NULL,
  `abordado` varchar(2) COLLATE utf8_spanish_ci NOT NULL DEFAULT 'NO'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `reservacion`
--

INSERT INTO `reservacion` (`IDReservacion`, `Nombre`, `Correo`, `Telefono`, `fechaReservacion`, `NTarjeta`, `Fecha`, `CVV`, `IDVuelo`, `abordado`) VALUES
(1, 'Carlos Ramirez', 'carlos@gmail.com', '123333', '2022-04-22 21:37:10', '2147483647', '12/11', '123', 1, 'SI'),
(2, 'Ely', 'ely@gmail.com', '+52111111', '2022-04-22 21:37:10', '1111222233334444', '11/11', '123', 1, 'NO'),
(3, 'Bryant Amaro ', 'amaro@runrun.com', '+52 1122333', '2022-04-22 21:38:55', '1234567891123456', '11/22', '123', 4, 'SI'),
(4, 'Steph', 'steph@runrun.com', '+52 1122333', '2022-04-22 21:42:02', '1234567891123456', '11/22', '123', 4, 'NO'),
(5, 'mama', 'sandwich@runrun.com', '+52 1122333', '2022-04-22 21:43:12', '1234567891123456', '11/22', '123', 4, 'NO'),
(6, 'Martin', 'tuki@runrun.com', '+52 1122333', '2022-04-22 23:14:56', '1234567891123456', '11/22', '123', 4, 'NO'),
(7, 'Emilio', 'emilio@garra.com', '123333', '2022-04-22 23:18:16', '1111222233334444', '11/33', '123', 6, 'SI'),
(8, 'Emilio Guerra', 'emilio@garra.com', '123333', '2022-04-22 23:20:57', '1111222233334444', '11/33', '123', 6, 'NO'),
(9, 'Emilio beta', 'emilio@garra.com', '123333', '2022-04-22 23:21:48', '1111222233334444', '11/33', '123', 6, 'NO'),
(10, 'Gabriel', 'gabriel@pro.com', '+12 123333', '2022-04-23 01:15:55', '1111222233334444', '11/33', '123', 6, 'NO'),
(11, 'Amaro run run', 'amaro@hamburguesa.com', '+1 123333554', '2022-04-23 14:20:49', '1111222233334444', '10/30', '123', 16, 'SI'),
(12, 'Ana Rios', 'Ana@gmail.coma', '123333344', '2022-04-23 15:30:36', '9999888877775555333', '12/12', '123', 3, 'SI');

-- --------------------------------------------------------

--
-- Table structure for table `vuelos`
--

CREATE TABLE `vuelos` (
  `idvuelo` int(11) NOT NULL,
  `destino` varchar(255) COLLATE utf8_spanish_ci NOT NULL,
  `fecha` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `hora` varchar(10) COLLATE utf8_spanish_ci NOT NULL,
  `aerolineaDestino` varchar(255) COLLATE utf8_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Dumping data for table `vuelos`
--

INSERT INTO `vuelos` (`idvuelo`, `destino`, `fecha`, `hora`, `aerolineaDestino`) VALUES
(1, 'CDMX', '2022-10-01', '12:10', 'aeromexico'),
(2, 'Monterrey', '2022-04-02', '10:30', 'vivaerobus'),
(3, 'Guadalajara', '2022-04-03', '10:30', 'vivaerobus'),
(4, 'Tijuana', '2022-04-04', '11:00', 'avion'),
(5, 'Tijuana', '2022-04-05', '11:00', 'avion'),
(6, 'La paz', '2022-04-05', '11:00', 'avion'),
(7, 'Cancun', '2022-04-05', '11:33', 'Aeromexico'),
(8, 'Dubai', '2022-10-28', '12:33', 'calafia'),
(9, 'Toronto', '2022-05-03', '10:00', 'Delta Airlines'),
(10, 'Quebec', 'mayo 4', '11:33', 'Delta Airlines'),
(11, 'San Andreas', 'mayo 6', '10:30', 'Fiction Airways'),
(12, 'San Fierro', 'mayo 6', '13:30', 'Fiction Airways'),
(13, 'Las Venturas', 'mayo 6', '14:30', 'Fiction Airways'),
(14, 'Liberty City', 'mayo 6 ', '17:00', 'Fiction Airways'),
(15, 'Rabat', 'mayo 7', '01:10', 'American Airways'),
(16, 'Berlin', 'mayo 30', '17:30', 'Aeromexico'),
(17, 'Puerto Vallarta', 'mayo 20', '10:30', 'Aeromexico');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adminuser`
--
ALTER TABLE `adminuser`
  ADD PRIMARY KEY (`idUser`);

--
-- Indexes for table `reservacion`
--
ALTER TABLE `reservacion`
  ADD PRIMARY KEY (`IDReservacion`);

--
-- Indexes for table `vuelos`
--
ALTER TABLE `vuelos`
  ADD PRIMARY KEY (`idvuelo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adminuser`
--
ALTER TABLE `adminuser`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `reservacion`
--
ALTER TABLE `reservacion`
  MODIFY `IDReservacion` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `vuelos`
--
ALTER TABLE `vuelos`
  MODIFY `idvuelo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
