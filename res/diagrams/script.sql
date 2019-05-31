-- Database: ds

-- DROP DATABASE ds;

/*CREATE DATABASE ds
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Portuguese_Brazil.1252'
    LC_CTYPE = 'Portuguese_Brazil.1252'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
*/

DROP TABLE IF EXISTS Medico CASCADE;
DROP TABLE IF EXISTS Paciente CASCADE;
DROP TABLE IF EXISTS Consulta CASCADE;
DROP TABLE IF EXISTS Funcionario CASCADE;

-- -----------------------------------------------------
-- Table `ds`.`medico`
-- -----------------------------------------------------
DROP TABLE IF EXISTS "ds".medico ;

CREATE TABLE Medico (
    CRM bigint NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    Especialidade VARCHAR(20) NOT NULL,
    militar VARCHAR(20) NOT NULL,
    PRIMARY KEY (CRM)
);


-- -----------------------------------------------------
-- Table `ds`.`paciente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS "ds".paciente ;

CREATE TABLE Paciente (
    CPF bigint NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    dt_nasc DATE NOT NULL,
    sexo CHAR NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    militar VARCHAR(20) NOT NULL,
    PRIMARY KEY (CPF)
);

-- -----------------------------------------------------
-- Table `ds`.`consulta`
-- -----------------------------------------------------
CREATE TABLE Consulta (
    id SERIAL,
    CPF_pac bigint NOT NULL,
    CRM int NOT NULL,
    Data DATE NOT NULL,
    Hora TIME NOT NULL,
    status VARCHAR(10) NOT NULL,
    CPF_staff bigint NOT NULL,
    PRIMARY KEY (id)
);

-- -----------------------------------------------------
-- Table `ds`.`Funcionario`
-- -----------------------------------------------------
CREATE TABLE Funcionario (
    CPF bigint NOT NULL,
    Nome VARCHAR(50) NOT NULL,
    dt_nasc DATE NOT NULL,
    sexo CHAR NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    militar VARCHAR(20) NOT NULL,
    PRIMARY KEY (CPF)
);

ALTER TABLE Consulta ADD FOREIGN KEY (CRM) REFERENCES Medico(CRM);
ALTER TABLE Consulta ADD FOREIGN KEY (CPF_pac) REFERENCES Paciente(CPF);
ALTER TABLE Consulta ADD FOREIGN KEY (CPF_staff) REFERENCES Funcionario(CPF);


-- -----------------------------------------------------
-- Inserts
-- -----------------------------------------------------

delete from Paciente;
delete from Medico;
delete from Funcionario;
delete from Consulta;

insert into Paciente 
values (13420296746,'Matheus Vidal','1995/03/28','M','Rua H8B,203 - SJC,SP','(21)99330-7585','matheusvidaldemenezes@gmail.com','alunoITA'),
(43967557839,'Adriano Soares','1996/03/08','M','Rua H8B,214 - SJC,SP','(18)99606-3534','srodrigues@gmail.com','alunoITA'),
(04339241698,'Pedro Alves','1997/04/04','M','Rua H8B,203 - SJC,SP','(18)99605-7649','alvesouza@gmail.com','alunoITA');

insert into Medico 
values (16863158,'Charlie','odontologista','1tenente'),
(15846758,'Jonas','ortopedista','2tenente'),
(15523418,'Nathalia','oftalmologista','capitao');

insert into Funcionario
values (13420296749,'Kelly','1969/05/15','F','Rua H9,105- SJC,SP','(12)99780-7368','kelly@gmail.com','civil');

insert into Consulta (CPF_pac,CRM,Data,Hora,status,CPF_staff) 
values (13420296746,16863158,'2019/05/27','11:00:00','aberto',13420296749),
(43967557839,15846758,'2019/05/28','15:30:00','marcado',13420296749);


-- -----------------------------------------------------
-- Query
-- -----------------------------------------------------

--select * from Paciente;
--select * from medico;
select * from Consulta;

select p.Nome, k.Nome, data, hora 
from
	(medico as m inner join consulta as c on (m.CRM=c.CRM) ) as k
	inner join paciente as p on (k.CPF_pac=p.CPF)
where status = 'marcado'











