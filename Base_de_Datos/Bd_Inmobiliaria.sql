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
   
    
create table Estado 
	(
    Id_Estado int not null auto_increment primary key,
    Nombre_Estado varchar(30)
    );
INSERT INTO `bd_inmobiliaria`.`estado` (`Id_Estado`, `Nombre_Estado`) VALUES ('1', 'Disponible');
INSERT INTO `bd_inmobiliaria`.`estado` (`Id_Estado`, `Nombre_Estado`) VALUES ('2', 'Señada');
INSERT INTO `bd_inmobiliaria`.`estado` (`Id_Estado`, `Nombre_Estado`) VALUES ('3', 'Alquilado');
INSERT INTO `bd_inmobiliaria`.`estado` (`Id_Estado`, `Nombre_Estado`) VALUES ('4', 'Vendido');
    
    
create table OperatoriaComercial
	(
    Id_Operatoria_Comercial int not null auto_increment primary key,
    Nombre_Operatoria_Comercial varchar(30)
    );
INSERT INTO `bd_inmobiliaria`.`operatoriacomercial` (`Id_Operatoria_Comercial`, `Nombre_Operatoria_Comercial`) VALUES ('1', 'Venta');
INSERT INTO `bd_inmobiliaria`.`operatoriacomercial` (`Id_Operatoria_Comercial`, `Nombre_Operatoria_Comercial`) VALUES ('2', 'Alquiler');
INSERT INTO `bd_inmobiliaria`.`operatoriacomercial` (`Id_Operatoria_Comercial`, `Nombre_Operatoria_Comercial`) VALUES ('3', 'En Disponibilidad');

create table Propietario
	(
    Id_Propietario int not null auto_increment primary key,
    Nombre varchar(40),
    Direccion varchar(50),
    Contacto int
    );
INSERT INTO `bd_inmobiliaria`.`propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('1', 'Fernando Vexenat', 'Av rancagua 2000', '4887766');
INSERT INTO `bd_inmobiliaria`.`propietario` (`Id_Propietario`, `Nombre`, `Direccion`, `Contacto`) VALUES ('2', 'Carolina Nis', 'Av Ejercito Arg. 4567', '4778899');

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