CREATE DATABASE Bd_Inmobiliaria;
USE Bd_Inmobiliaria;

create table Tipo
	(
    Id_Tipo int not null auto_increment primary key,
    Nombre_Tipo varchar(30)
    );
    
    
create table Estado 
	(
    Id_Estado int not null auto_increment primary key,
    Nombre_Estado varchar(30)
    );
    
    
create table OperatoriaComercial
	(
    Id_Operatoria_Comercial int not null auto_increment primary key,
    Nombre_Operatoria_Comercial varchar(30)
    );

create table Propietario
	(
    Id_Propietario int not null auto_increment primary key,
    Nombre varchar(40),
    Direccion varchar(50),
    Contacto int
    );

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