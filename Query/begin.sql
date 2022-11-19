create database checkup;
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
PRIMARY KEY (id),
foreign key (grupo) references GRUPO(nome)
);

create table META(
	data1 date NOT NULL,
    id mediumint NOT NULL,
    vendas float,
    PRIMARY KEY (data1,id),
    FOREIGN KEY (id) REFERENCES PRODUTO(id)
);

create table PEDIDO(
	codigo varchar(20) NOT NULL,
    id_produto mediumint NOT NULL,
    datat date,
    id_cliente mediumint NOT NULL,
    quantidade int NOT NULL,
    preco float NOT NULL,
    custo float NOT NULL,
    margem float,
    primary key (codigo,id_produto),
    foreign key (id_cliente) references CLIENTE(id),
    foreign key (id_produto) references PRODUTO(id)
);
