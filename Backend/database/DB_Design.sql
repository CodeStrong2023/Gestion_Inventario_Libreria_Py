-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema BD_Libreria
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema BD_Libreria
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `BD_Libreria` DEFAULT CHARACTER SET utf8 ;
USE `BD_Libreria` ;

-- -----------------------------------------------------
-- Table `BD_Libreria`.`Articulo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Articulo` (
  `idArticulo` INT NOT NULL AUTO_INCREMENT,
  `alto` VARCHAR(45) NULL,
  `ancho` VARCHAR(45) NULL,
  `peso` VARCHAR(45) NULL,
  `precio` DOUBLE NULL,
  `tipo` VARCHAR(50) NULL,
  PRIMARY KEY (`idArticulo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Pais`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Pais` (
  `idPais` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idPais`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Ciudad`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Ciudad` (
  `idCiudad` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `Pais_idPais` INT NOT NULL,
  PRIMARY KEY (`idCiudad`, `Pais_idPais`),
  INDEX `fk_Ciudad_Pais1_idx` (`Pais_idPais` ASC) VISIBLE,
  CONSTRAINT `fk_Ciudad_Pais1`
    FOREIGN KEY (`Pais_idPais`)
    REFERENCES `BD_Libreria`.`Pais` (`idPais`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Direccion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Direccion` (
  `idDireccion` INT NOT NULL AUTO_INCREMENT,
  `calle` VARCHAR(45) NULL,
  `numero` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `Ciudad_idCiudad` INT NOT NULL,
  `Ciudad_Pais_idPais` INT NOT NULL,
  PRIMARY KEY (`idDireccion`, `Ciudad_idCiudad`, `Ciudad_Pais_idPais`),
  INDEX `fk_Direccion_Ciudad1_idx` (`Ciudad_idCiudad` ASC, `Ciudad_Pais_idPais` ASC) VISIBLE,
  CONSTRAINT `fk_Direccion_Ciudad1`
    FOREIGN KEY (`Ciudad_idCiudad` , `Ciudad_Pais_idPais`)
    REFERENCES `BD_Libreria`.`Ciudad` (`idCiudad` , `Pais_idPais`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Rol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Rol` (
  `idRol` INT NOT NULL AUTO_INCREMENT,
  `rol` VARCHAR(45) NULL,
  PRIMARY KEY (`idRol`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Usuario` (
  `idUsuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `fechaNacimiento` DATE NULL,
  `imagenUsuario` VARCHAR(250) NULL,
  `Direccion_idDireccion` INT NOT NULL,
  `Rol_idRol` INT NOT NULL,
  PRIMARY KEY (`idUsuario`, `Direccion_idDireccion`, `Rol_idRol`),
  INDEX `fk_Usuario_Direccion1_idx` (`Direccion_idDireccion` ASC) VISIBLE,
  INDEX `fk_Usuario_Rol1_idx` (`Rol_idRol` ASC) VISIBLE,
  CONSTRAINT `fk_Usuario_Direccion1`
    FOREIGN KEY (`Direccion_idDireccion`)
    REFERENCES `BD_Libreria`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Usuario_Rol1`
    FOREIGN KEY (`Rol_idRol`)
    REFERENCES `BD_Libreria`.`Rol` (`idRol`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Empresa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Empresa` (
  `idEmpresa` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `cuil` INT NULL,
  `logoEmpresa` VARCHAR(250) NULL,
  `Direccion_idDireccion` INT NOT NULL,
  PRIMARY KEY (`idEmpresa`, `Direccion_idDireccion`),
  INDEX `fk_Empresa_Direccion1_idx` (`Direccion_idDireccion` ASC) VISIBLE,
  CONSTRAINT `fk_Empresa_Direccion1`
    FOREIGN KEY (`Direccion_idDireccion`)
    REFERENCES `BD_Libreria`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Almacenamiento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Almacenamiento` (
  `idAlmacenamiento` INT NOT NULL AUTO_INCREMENT,
  `capacidadTotalM3` VARCHAR(45) NULL,
  `usoM3` VARCHAR(45) NULL,
  `Empresa_idEmpresa` INT NOT NULL,
  `Direccion_idDireccion` INT NOT NULL,
  PRIMARY KEY (`idAlmacenamiento`, `Empresa_idEmpresa`, `Direccion_idDireccion`),
  INDEX `fk_Almacenamiento_Empresa_idx` (`Empresa_idEmpresa` ASC) VISIBLE,
  INDEX `fk_Almacenamiento_Direccion1_idx` (`Direccion_idDireccion` ASC) VISIBLE,
  CONSTRAINT `fk_Almacenamiento_Empresa`
    FOREIGN KEY (`Empresa_idEmpresa`)
    REFERENCES `BD_Libreria`.`Empresa` (`idEmpresa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Almacenamiento_Direccion1`
    FOREIGN KEY (`Direccion_idDireccion`)
    REFERENCES `BD_Libreria`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Envio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Envio` (
  `idEnvio` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NULL,
  `estado` VARCHAR(45) NULL,
  `fechaDespacho` DATE NULL,
  `fechaEntrega` DATE NULL,
  `Direccion_idDireccion` INT NOT NULL,
  PRIMARY KEY (`idEnvio`, `Direccion_idDireccion`),
  INDEX `fk_Envio_Direccion1_idx` (`Direccion_idDireccion` ASC) VISIBLE,
  CONSTRAINT `fk_Envio_Direccion1`
    FOREIGN KEY (`Direccion_idDireccion`)
    REFERENCES `BD_Libreria`.`Direccion` (`idDireccion`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Facturas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Facturas` (
  `idFacturas` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NULL,
  `fechaEmision` DATE NULL,
  `imagenFactura` VARCHAR(250) NULL,
  PRIMARY KEY (`idFacturas`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Pago`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Pago` (
  `idPago` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NULL,
  `cuotas` INT NULL,
  `Facturas_idFacturas` INT NOT NULL,
  `origen` ENUM("Compra", "Venta") NULL,
  PRIMARY KEY (`idPago`, `Facturas_idFacturas`),
  INDEX `fk_Pago_Facturas1_idx` (`Facturas_idFacturas` ASC) VISIBLE,
  CONSTRAINT `fk_Pago_Facturas1`
    FOREIGN KEY (`Facturas_idFacturas`)
    REFERENCES `BD_Libreria`.`Facturas` (`idFacturas`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Venta`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Venta` (
  `idVenta` INT NOT NULL AUTO_INCREMENT,
  `fechaVenta` DATE NULL,
  `Usuario_idUsuario` INT NOT NULL,
  `Envio_idEnvio` INT NOT NULL,
  `Articulo_idArticulo` INT NOT NULL,
  `Pago_idPago` INT NOT NULL,
  PRIMARY KEY (`idVenta`, `Usuario_idUsuario`, `Envio_idEnvio`, `Articulo_idArticulo`, `Pago_idPago`),
  INDEX `fk_Venta_Usuario1_idx` (`Usuario_idUsuario` ASC) VISIBLE,
  INDEX `fk_Venta_Envio1_idx` (`Envio_idEnvio` ASC) VISIBLE,
  INDEX `fk_Venta_Articulo1_idx` (`Articulo_idArticulo` ASC) VISIBLE,
  INDEX `fk_Venta_Pago1_idx` (`Pago_idPago` ASC) VISIBLE,
  CONSTRAINT `fk_Venta_Usuario1`
    FOREIGN KEY (`Usuario_idUsuario`)
    REFERENCES `BD_Libreria`.`Usuario` (`idUsuario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Venta_Envio1`
    FOREIGN KEY (`Envio_idEnvio`)
    REFERENCES `BD_Libreria`.`Envio` (`idEnvio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Venta_Articulo1`
    FOREIGN KEY (`Articulo_idArticulo`)
    REFERENCES `BD_Libreria`.`Articulo` (`idArticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Venta_Pago1`
    FOREIGN KEY (`Pago_idPago`)
    REFERENCES `BD_Libreria`.`Pago` (`idPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Editorial`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Editorial` (
  `idEditorial` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `imagenEditorial` VARCHAR(250) NULL,
  PRIMARY KEY (`idEditorial`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Proveedor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Proveedor` (
  `idProveedor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `contactoPrincipal` VARCHAR(45) NULL,
  PRIMARY KEY (`idProveedor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Devolucion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Devolucion` (
  `idDevolucion` INT NOT NULL AUTO_INCREMENT,
  `motivo` VARCHAR(45) NULL,
  `fechaDevolucion` DATE NULL,
  `cantidad` INT NULL,
  `Pago_idPago` INT NOT NULL,
  PRIMARY KEY (`idDevolucion`, `Pago_idPago`),
  INDEX `fk_Devolucion_Pago1_idx` (`Pago_idPago` ASC) VISIBLE,
  CONSTRAINT `fk_Devolucion_Pago1`
    FOREIGN KEY (`Pago_idPago`)
    REFERENCES `BD_Libreria`.`Pago` (`idPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`genero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`genero` (
  `idgenero` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  PRIMARY KEY (`idgenero`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Libro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Libro` (
  `idLibro` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NULL,
  `idioma` VARCHAR(45) NULL,
  `tapa` VARCHAR(45) NULL,
  `año` INT NULL,
  `isbn` VARCHAR(45) NULL,
  `paginas` VARCHAR(45) NULL,
  `edicion` VARCHAR(45) NULL,
  `edad_minima` INT NULL,
  `edad_maxima` INT NULL,
  `descripcion` VARCHAR(45) NULL,
  `imagen_tapa` VARCHAR(250) NULL,
  `Articulo_idArticulo` INT NOT NULL,
  `genero_idgenero` INT NOT NULL,
  `Editorial_idEditorial` INT NOT NULL,
  PRIMARY KEY (`idLibro`, `Articulo_idArticulo`, `genero_idgenero`, `Editorial_idEditorial`),
  INDEX `fk_Libro_Articulo1_idx` (`Articulo_idArticulo` ASC) VISIBLE,
  INDEX `fk_Libro_genero1_idx` (`genero_idgenero` ASC) VISIBLE,
  INDEX `fk_Libro_Editorial1_idx` (`Editorial_idEditorial` ASC) VISIBLE,
  UNIQUE INDEX `Articulo_idArticulo_UNIQUE` (`Articulo_idArticulo` ASC) VISIBLE,
  CONSTRAINT `fk_Libro_Articulo1`
    FOREIGN KEY (`Articulo_idArticulo`)
    REFERENCES `BD_Libreria`.`Articulo` (`idArticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Libro_genero1`
    FOREIGN KEY (`genero_idgenero`)
    REFERENCES `BD_Libreria`.`genero` (`idgenero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Libro_Editorial1`
    FOREIGN KEY (`Editorial_idEditorial`)
    REFERENCES `BD_Libreria`.`Editorial` (`idEditorial`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Autor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Autor` (
  `idAutor` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `imagenAutor` VARCHAR(250) NULL,
  PRIMARY KEY (`idAutor`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Compra`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Compra` (
  `CompraId` INT NOT NULL AUTO_INCREMENT,
  `Almacenamiento_idAlmacenamiento` INT NOT NULL,
  `Articulo_idArticulo` INT NOT NULL,
  `fecha` DATE NULL,
  `cantidad` INT NULL,
  `precioUnitario` DOUBLE NULL,
  `Pago_idPago` INT NOT NULL,
  `Proveedor_idProveedor` INT NOT NULL,
  PRIMARY KEY (`CompraId`, `Almacenamiento_idAlmacenamiento`, `Articulo_idArticulo`, `Pago_idPago`, `Proveedor_idProveedor`),
  INDEX `fk_Almacenamiento_has_Articulo_Articulo1_idx` (`Articulo_idArticulo` ASC) VISIBLE,
  INDEX `fk_Almacenamiento_has_Articulo_Almacenamiento1_idx` (`Almacenamiento_idAlmacenamiento` ASC) VISIBLE,
  INDEX `fk_Compra_Pago1_idx` (`Pago_idPago` ASC) VISIBLE,
  INDEX `fk_Compra_Proveedor1_idx` (`Proveedor_idProveedor` ASC) VISIBLE,
  CONSTRAINT `fk_Almacenamiento_has_Articulo_Almacenamiento1`
    FOREIGN KEY (`Almacenamiento_idAlmacenamiento`)
    REFERENCES `BD_Libreria`.`Almacenamiento` (`idAlmacenamiento`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Almacenamiento_has_Articulo_Articulo1`
    FOREIGN KEY (`Articulo_idArticulo`)
    REFERENCES `BD_Libreria`.`Articulo` (`idArticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Compra_Pago1`
    FOREIGN KEY (`Pago_idPago`)
    REFERENCES `BD_Libreria`.`Pago` (`idPago`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Compra_Proveedor1`
    FOREIGN KEY (`Proveedor_idProveedor`)
    REFERENCES `BD_Libreria`.`Proveedor` (`idProveedor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Revista`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Revista` (
  `idRevista` INT NOT NULL AUTO_INCREMENT,
  `titulo` VARCHAR(45) NULL,
  `numero` INT NULL,
  `anio` INT NULL,
  `mes` INT NULL,
  `dia` INT NULL,
  `Articulo_idArticulo` INT NOT NULL,
  `Editorial_idEditorial` INT NOT NULL,
  `genero_idgenero` INT NOT NULL,
  PRIMARY KEY (`idRevista`, `Articulo_idArticulo`, `Editorial_idEditorial`, `genero_idgenero`),
  INDEX `fk_Revista_Articulo1_idx` (`Articulo_idArticulo` ASC) VISIBLE,
  INDEX `fk_Revista_Editorial1_idx` (`Editorial_idEditorial` ASC) VISIBLE,
  INDEX `fk_Revista_genero1_idx` (`genero_idgenero` ASC) VISIBLE,
  UNIQUE INDEX `Articulo_idArticulo_UNIQUE` (`Articulo_idArticulo` ASC) VISIBLE,
  CONSTRAINT `fk_Revista_Articulo1`
    FOREIGN KEY (`Articulo_idArticulo`)
    REFERENCES `BD_Libreria`.`Articulo` (`idArticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Revista_Editorial1`
    FOREIGN KEY (`Editorial_idEditorial`)
    REFERENCES `BD_Libreria`.`Editorial` (`idEditorial`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Revista_genero1`
    FOREIGN KEY (`genero_idgenero`)
    REFERENCES `BD_Libreria`.`genero` (`idgenero`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `BD_Libreria`.`Autor_has_Libro`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `BD_Libreria`.`Autor_has_Libro` (
  `Autor_idAutor` INT NOT NULL,
  `Libro_idLibro` INT NOT NULL,
  `Libro_Articulo_idArticulo` INT NOT NULL,
  PRIMARY KEY (`Autor_idAutor`, `Libro_idLibro`, `Libro_Articulo_idArticulo`),
  INDEX `fk_Autor_has_Libro_Libro1_idx` (`Libro_idLibro` ASC, `Libro_Articulo_idArticulo` ASC) VISIBLE,
  INDEX `fk_Autor_has_Libro_Autor1_idx` (`Autor_idAutor` ASC) VISIBLE,
  CONSTRAINT `fk_Autor_has_Libro_Autor1`
    FOREIGN KEY (`Autor_idAutor`)
    REFERENCES `BD_Libreria`.`Autor` (`idAutor`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Autor_has_Libro_Libro1`
    FOREIGN KEY (`Libro_idLibro` , `Libro_Articulo_idArticulo`)
    REFERENCES `BD_Libreria`.`Libro` (`idLibro` , `Articulo_idArticulo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
