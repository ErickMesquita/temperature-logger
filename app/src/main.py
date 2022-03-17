import os
import urllib.parse
import requests
import time, datetime
from sqlalchemy.exc import NoSuchTableError
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData, Table, Column, Float, SMALLINT, TIMESTAMP
from sqlalchemy.orm import Session
from sqlalchemy import insert, text

from retry import retry

@retry((requests.exceptions.Timeout, requests.exceptions.ConnectionError), backoff=1.3)
def request_api(api_host: str, api_endpoint: str) -> float:
	response = requests.get(f"http://{api_host}/{api_endpoint}", timeout=4.5)
	return float(response.text)
	
def request_api_safely(api_host: str, api_endpoint: str, logger=None) -> float:
	try:
		dados = request_api(api_host, api_endpoint)
	except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
		dados = None
		msg = f"{str(e)}. Não foi possível conectar à API"
		if logger:
			logger.error(msg)
		else:
			print(msg)
	finally:
		return dados

def get_values(api_host: str):
	temperature = request_api_safely(api_host, "temperature")
	humidity    = request_api_safely(api_host, "humidity")
	print(f"Temperatura= {temperature}\tUmidade= {humidity}")
	return {"temperature": temperature,
			"humidity": humidity}

def db_create_table_temperatura(metadata_obj):
	temperatura_tabela = Table(
		"Temperatura",
		metadata_obj,
		Column("Horario", TIMESTAMP(timezone=True), primary_key=True, key="Horário"),
		Column("Temperatura", Float, comment="Temperatura em ºC"),
		Column("Umidade", SMALLINT, comment="Umidade em %")
	)
	return temperatura_tabela

def db_get_table_temperatura(metadata_obj, engine):
	try:
		temperatura_tabela = Table(
			"Temperatura",
			metadata_obj,
			autoload_with=engine
		)
	except NoSuchTableError:
		print("Tabela 'Temperatura' não encontrada, criando tabela em branco...")
		temperatura_tabela = db_create_table_temperatura(metadata_obj)
		temperatura_tabela.create(engine)

	return temperatura_tabela


def db_create_engine():
	user = urllib.parse.quote_plus(os.environ.get("DB_USER", "app"))
	password = urllib.parse.quote_plus(os.environ.get("DB_PASS", "senha+super+secreta2"))
	host = urllib.parse.quote_plus(os.environ.get("DB_HOST", "db"))
	port = urllib.parse.quote_plus(os.environ.get("DB_PORT", "5432"))
	database = urllib.parse.quote_plus(os.environ.get("DB_DATABASE", "Medidas"))
	encoding = os.environ.get("DB_ENCODING", "utf8")
	echo = os.environ.get("DB_ECHO", 1)

	url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

	return create_engine(url, encoding=encoding, echo=echo)
	

def db_initial_connect(engine):
	time.sleep(7)
	retries = 45
	while True:
		try:
			with engine.connect() as conn:
				result = conn.execute(text("select 'hello world'"))
				print(result.all())
		except:
			if retries == 0:
				print("Não foi possível conectar ao banco de dados")
				raise IOError
			retries -= 1
			time.sleep(1)
		else:
			return

def main():
	print("Hello World")
	
	engine = db_create_engine()

	metadata_obj = MetaData()

	db_initial_connect(engine)

	temperatura_tabela = db_get_table_temperatura(metadata_obj, engine)

	api_host = "192.168.1.76"
	periodo_sec = 90
	start_time = time.time()

	while(True):
		dict_values = get_values(api_host)
		with Session(engine) as session:
			session.execute(insert(temperatura_tabela).values(
				Horario=     datetime.datetime.now(),
				Temperatura= dict_values.get("temperature"),
				Umidade=     dict_values.get("humidity")
			))
			session.commit()
		time.sleep(periodo_sec - ((time.time() - start_time) % periodo_sec))

				






if __name__ == "__main__":
   main()