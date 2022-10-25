CREATE DATABASE Bd_Inmobiliaria;
USE Bd_Inmobiliaria;

create table Tipo
	(
    Id_Tipo int not null auto_increment primary key,
    Nombre_Tipo varchar(30)
    );
INSERT INTO `bd_inmobiliaria`.`tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES ('1', 'Casa');
INSERT INTO `bd_inmobiliaria`.`tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES ('2', 'Departamento');
INSERT INTO `bd_inmobiliaria`.`tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES ('3', 'Duplex');
INSERT INTO `bd_inmobiliaria`.`tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES ('4', 'Monoambiente');
INSERT INTO `bd_inmobiliaria`.`tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES ('5', 'Chalet');
INSERT INTO `bd_inmobiliaria`.`tipo` (`Id_Tipo`, `Nombre_Tipo`) VALUES ('6', 'Local Comercial');   
    
create table Estado 
	(
    Id_Estado int not null auto_increment primary key,
    Nombre_Estado varchar(30)
    );
INSERT INTO `bd_inmobiliaria`.`estado` (`Id_Estado`, `Nombre_Estado`) VALUES ('1', 'Disponible');
INSERT INTO `bd_inmobiliaria`.`estado` (`Id_Estado`, `Nombre_Estado`) VALUES ('2', 'No Disponible');

    
    
create table OperatoriaComercial
	(
    Id_Operatoria_Comercial int not null auto_increment primary key,
    Nombre_Operatoria_Comercial varchar(30)
    );
INSERT INTO `bd_inmobiliaria`.`operatoriacomercial` (`Id_Operatoria_Comercial`, `Nombre_Operatoria_Comercial`) VALUES ('1', 'Venta');
INSERT INTO `bd_inmobiliaria`.`operatoriacomercial` (`Id_Operatoria_Comercial`, `Nombre_Operatoria_Comercial`) VALUES ('2', 'Alquiler');

create table Propietario
	(
    Id_Propietario int not null auto_increment primary key,
    Nombre varchar(40),
    Direccion varchar(50),
    Contacto int
    );
INSERT INTO `bd_inmobiliaria`.`propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('1', 'Fernando Vexenat', 'Av rancagua 2000', '4887766');
INSERT INTO `bd_inmobiliaria`.`propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('2', 'Carolina Nis', 'Av Ejercito Arg. 4567', '4778899');
INSERT INTO `bd_inmobiliaria`.`propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('3', 'Leonardo Gonzalez', '27 de Abril 1345', '4332456');
INSERT INTO `bd_inmobiliaria`.`propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('4', 'Andres Montaño', 'San Jeronimo 34', '4221234');
INSERT INTO `bd_inmobiliaria`.`propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('5', 'Mirta Legrand', 'Av Colon 1250', '4323367');

create table Propiedad
	(
    Id_Propiedad int not null auto_increment primary key,
    Id_Tipo int,
    Id_Estado int,
    Id_Operacion_Comercial int,
    Id_Propietario int,
    Nombre varchar(20),
    Direccion varchar(30),
    Contacto int
    );

alter table Propiedad add foreign key (Id_Tipo) references Tipo (Id_Tipo);

alter table Propiedad add foreign key (Id_Estado) references Estado (Id_Estado);

alter table Propiedad add foreign key (Id_Operacion_Comercial) references OperatoriaComercial (Id_Operatoria_Comercial);

alter table Propiedad add foreign key (Id_Propietario) references	Propietario (Id_Propietario);

INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`) VALUES ('1', '5', '1', '1');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`, `Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('2', '4', '2', '2', '1', 'Fernando Vexenat', 'Av rancagua 2000', '4887766');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`, `Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('3', '3', '2', '1', '2', 'Carolina Nis', 'Av Ejercito Arg. 4567', '4778899');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`) VALUES ('4', '2', '1', '1',);
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`, `Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('5', '1', '2', '2', '3', 'Leonardo Gonzalez', '27 de Abril 1345', '4332456');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`, `Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('6', '6', '2', '1', '4', 'Andres Montaño', 'San Jeronimo 34', '4221234');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`) VALUES ('7', '5', '1', '1');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`, `Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('8', '3', '2', '2', '5', 'Mirta Legrand', 'Av Colon 1250', '4323367');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`) VALUES ('9', '2', '1', '1');
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`) VALUES ('10', '6', '1', '1');

# Ingresar una propiedad
INSERT INTO `bd_inmobiliaria`.`propiedad` (`Id_Propiedad`, `Id_Tipo`, `Id_Estado`, `Id_Operacion_Comercial`) VALUES ('11', '2', '1', '1');
# Modificar una propiedad
UPDATE propiedad SET Id_Tipo = 1 WHERE Id_Propiedad = 11;
# Eliminar una propiedad 
DELETE FROM propiedad WHERE Id_Propiedad = 11;
# Listado de propiedades TOTALES, sin distinción de estados.
SELECT * FROM bd_inmobiliaria.propiedad;
# Listado de propiedades DISPONIBLES para la venta.
SELECT * FROM bd_inmobiliaria.propiedad WHERE Id_Estado = 1 AND Id_Operacion_Comercial = 3;
# Listado de propiedades DISPONIBLES para alquiler.
SELECT * FROM bd_inmobiliaria.propiedad WHERE Id_Estado = 1 AND Id_Operacion_Comercial = 2;
# Listado de propiedades vendidas.
SELECT * FROM bd_inmobiliaria.propiedad WHERE Id_Estado = 3;
# Listado de propiedades alquiladas.
SELECT * FROM bd_inmobiliaria.propiedad WHERE Id_Estado = 2;