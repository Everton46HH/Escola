drop database if exists Locadora;
create database Locadora;
use Locadora;
CREATE TABLE cliente 
( 
 idcli int primary key AUTO_INCREMENT,
 cpf char(14) unique not null,  
 nome varchar(30),  
 endereco VARCHAR (40) not null,
 cidade VARCHAR(30) not null,
 estado VARCHAR (2) not null,
 email VARCHAR (40) not null
); 
CREATE TABLE carro 
( 
 idcarro int primary key AUTO_INCREMENT,
 placa char(7) unique NOT NULL,  
 modelo VARCHAR(25) NOT NULL,
 ano INT NOT NULL, 
 cor varchar(20) NOT NULL,   
 km INT NOT NULL,  
 valordiaria float not null
); 



CREATE TABLE locacao 
( 
 numero INT PRIMARY KEY,
 data_retirada date not null,  
 data_devolucao date not null,
 qtdedias int not null,
 valorLoc FLOAT not null,  
 idcli int not null,
 idcarro int not null,
 foreign key (idcli) references cliente (idcli),
 foreign key (idcarro) references carro (idcarro)
);

create table telefone(
numero char(12),
idtelefone int primary key,
idcli int,
foreign key (idcli) references cliente (idcli)
);

describe Locacao;


insert into Cliente values(default,"123.456.789-00","Everton","Rua Domingues ALguma Coisa","Vargem","SP","evertonbonitao@gmail.com");
insert into Cliente values(default,"123.456.789-01","Aynna","Sitio Sao Jose","Camanducaia","SP","AynnaUrubu@gmail.com");
insert into Cliente values(default,"123.456.789-02","Eduardo Venceslau","Lobisomen Da Silva","Joanopolis","SP","RussoDoIF@gmail.com");
insert into Cliente values(default,"123.456.789-03","Bruna Camargo ","Rua dos Lirios","Braganca Paulista","SP","Brunagalindo@gmail.com");
insert into Cliente values(default,"123.456.789-04","Eduardo Lopes ","Rua Joao Siriani","Braganca Paulista","SP","EldViana@gmail.com");
insert into Cliente values(default,"123.456.789-05","Fernanda Nascimento","Rua Luiz Enzo","Braganca Paulista","SP","nascimento.fernanda@gmail.com");


insert into Locacao values(1,"2024-07-04","2024-07-03",1,500.00,2,1);
select Cliente.idcli,data_Retirada,data_Devolucao,qtdeDias,valorLoc,placa,modelo,valordiaria,cpf,nome
from Locacao,carro, Cliente
where Locacao.idcli = Cliente.idcli and
Locacao.idcarro = carro.idcarro;

insert into carro values ( default,"IFSP123","Maverick VB", 1975, "Verde", 32100, 250.00);
insert into carro values ( default,"IFSP321","Varlant TL",1972, "Verde" , 32700, 230.00);
insert into carro values ( default,"TPASSA3","Dogde LT",1980,"Verde Limao", 45800, 550.00);

UPDATE carro SET cor =  "Verde Abacate" where placa="IFSP123";
UPDATE carro SET modelo = "Dodge Viper RT/10" where placa = "TPASSA3";
UPDATE Cliente SET nome = "Eduardo Venceslau Marques Bueno" where cpf = "123.456.789-02";
UPDATE carro SET tcomb = "Gasolina"  where placa="IFSP123";
UPDATE carro SET tcomb = "Gasolina"  where placa="IFSP321";
UPDATE carro SET tcomb = "Gasolina"  where placa="TPASSA3";


select * from carro;
select * from Cliente;
select * from Locacao;
describe carro;

ALTER TABLE carro
add tcomb VARCHAR (20) NOT NULL;

# Comandos DNL
start transaction;
commit;
rollback;

# Comandos DDL

# create
# alter
# drop

drop database Locadora;


