-- Database: ds

-- DROP DATABASE ds;

/*
CREATE DATABASE ds
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
DROP TABLE IF EXISTS Logado CASCADE;

-- ----------------------------------------------------- 
-- Table `ds`.`medico`
-- -----------------------------------------------------
DROP TABLE IF EXISTS "ds".medico ;

CREATE TABLE Medico (
	CPF varchar(14) unique NOT NULL,
	senha varchar NOT NULL,
	SARAM int unique,
    Nome VARCHAR(50) NOT NULL,
	militar VARCHAR(20) NOT NULL,
	CRM int unique NOT NULL,
    Especialidade VARCHAR(20) NOT NULL,
    PRIMARY KEY (CRM)
);


-- -----------------------------------------------------
-- Table `ds`.`paciente`
-- -----------------------------------------------------
DROP TABLE IF EXISTS "ds".paciente ;

CREATE TABLE Paciente (
    CPF varchar(14) unique NOT NULL,
	senha varchar NOT NULL,
	SARAM int unique,
    Nome VARCHAR(50) NOT NULL,
    dt_nasc DATE NOT NULL,
    sexo CHAR NOT NULL,
    endereco VARCHAR(50) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    email VARCHAR(50) NOT NULL,
    militar VARCHAR(20) NOT NULL,
	valido BOOLEAN,
    PRIMARY KEY (CPF)
);

-- -----------------------------------------------------
-- Table `ds`.`consulta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS "ds".consulta ;

CREATE TABLE Consulta (
    id SERIAL,
    CPF_pac varchar(14) unique NOT NULL,
    CRM int unique NOT NULL,
    dia varchar(15) NOT NULL,
    hora_inicio varchar(10) NOT NULL,
	hora_fim varchar(10) NOT NULL,
	descricao varchar(70),
    PRIMARY KEY (id)
);

-- -----------------------------------------------------
-- Table `ds`.`logado`
-- -----------------------------------------------------
DROP TABLE IF EXISTS "ds".logado ;

CREATE TABLE Logado (
    CPF varchar(14) unique NOT NULL,
	session_hash varchar(60) unique NOT NULL, 
    PRIMARY KEY (CPF)
);

--ALTER TABLE Logado ADD FOREIGN KEY (CPF) REFERENCES Paciente(CPF);
--ALTER TABLE Logado ADD FOREIGN KEY (CPF) REFERENCES Medico(CPF);
ALTER TABLE Consulta ADD FOREIGN KEY (CRM) REFERENCES Medico(CRM);
ALTER TABLE Consulta ADD FOREIGN KEY (CPF_pac) REFERENCES Paciente(CPF);

-- -----------------------------------------------------
-- Inserts
-- -----------------------------------------------------
/*
delete from Paciente;
delete from Medico;
delete from Consulta;

insert into Paciente values 
('134.202.967-46','$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDWYK',7654321,'Matheus Vidal','1995/03/28','M','Rua H8B,203 - SJC,SP','(21)99330-7585','matheusvidaldemenezes@gmail.com','alunoITA',false),
('439.675.578-39','$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDWYK',8654321,'Adriano Soares','1996/03/08','M','Rua H8B,214 - SJC,SP','(18)99606-3534','srodrigues@gmail.com','alunoITA',false),
('043.392.416-98','$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDWYK',9654321,'Pedro Alves','1997/04/04','M','Rua H8B,203 - SJC,SP','(18)99605-7649','alvesouza@gmail.com','alunoITA',false);

insert into Medico values 
('134.202.967-41',16863158,'$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDWYK',1234567,'Charlie','odontologista','1tenente'),
('134.202.967-42',15846758,'$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDWYK',1234568,'Jonas','ortopedista','2tenente'),
('134.202.967-43',15523418,'$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDWYK',1234569,'Nathalia','oftalmologista','capitao');

insert into Consulta (CPF_pac,CRM,dia,hora_inicio,hora_fim,descricao) values 
('134.202.967-46',16863158,'Segunda','11:00','11:30','deu ruim'),
('439.675.578-39',15846758,'Terça','15:30','16:00','Jacks');

insert into Logado values 
(13420296746,'$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDAAA'),
(13420296741,'$2b$12$9hihmAkRabPNb5MhIk0ui.mY7rEjDGdcctGaRR2/DHflaa9ldDBBB');
*/

-- -----------------------------------------------------
-- Query
-- -----------------------------------------------------

--select * from Paciente;
--select * from medico;
--select * from Consulta;

/*
select p.Nome, k.Nome, data, hora 
from
	(medico as m inner join consulta as c on (m.CRM=c.CRM) ) as k
	inner join paciente as p on (k.CPF_pac=p.CPF)
where status = 'marcado'
*/

/*
-- Retorna pacientes logados
select * from
(select * from paciente) as p inner join (select * from logado) as l on (p.CPF=l.CPF)
*/

/*
-- Retorna medicos logados
select * from
(select * from medico) as m inner join (select * from logado) as l on (m.CPF=l.CPF)
*/










