--CREATE DATABASE "Medidas" ENCODING 'UTF8';
--USE Medidas;

CREATE USER app WITH PASSWORD 'senha+super+secreta2';

--GRANT CONNECT ON DATABASE "Medidas" TO app;

CREATE TABLE "Temperatura"(
    "Horario" TIMESTAMP NOT NULL UNIQUE PRIMARY KEY, --COMMENT 'Horário de coleta das medidas.',
    "Temperatura" FLOAT, --COMMENT 'Temperatura medida em graus centígrados.',
    "Umidade" SMALLINT --COMMENT 'Umidade relativa do ar em porcentagem.'
);

GRANT SELECT, INSERT ON TABLE "Temperatura" TO app;


-- INSERT INTO Temperatura VALUES(
	-- TIMESTAMP("2022-03-02 17:48:30"),30.20,62.00
-- );