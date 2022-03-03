CREATE DATABASE Medidas;
USE Medidas;
CREATE TABLE Temperatura(
    Horario TIMESTAMP NOT NULL UNIQUE PRIMARY KEY COMMENT 'Horário de coleta das medidas.',
    Temperatura DECIMAL(4, 2) COMMENT 'Temperatura medida em graus centígrados.',
    Umidade DECIMAL(4, 2) UNSIGNED COMMENT 'Umidade relativa do ar em porcentagem.'
);


-- INSERT INTO Temperatura VALUES(
	-- TIMESTAMP("2022-03-02 17:48:30"),30.20,62.00
-- );