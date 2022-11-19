create database checkup;
show databases;
use checkup;

create table CLIENTE(
	id mediumint NOT NULL AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    PRIMARY KEY (id)
);

create table GRUPO(
nome varchar(2) NOT NULL,
imposto float,
PRIMARY KEY (nome)
);

create table PRODUTO(
id mediumint NOT NULL AUTO_INCREMENT,
grupo varchar(2) NOT NULL,
preco float NOT NULL,
custo float NOT NULL,
margem float,
PRIMARY KEY (id),
foreign key (grupo) references GRUPO(nome)
);