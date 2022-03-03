from sqlalchemy import create_engine

def main():
    print("Hello World!")
    print(f"SQLAlchemy importado com sucesso! sqlalchemy.__version__ = {sqlalchemy.__version__}")
    # print(f"__name__ = {__name__}")

    engine = create_engine("mysql+mysqldb://app:senha+super+secreta2@meu-mysql:3306/Medidas",
                            encoding='utf8', echo=True)
    
    








if __name__ == "__main__":
   main()