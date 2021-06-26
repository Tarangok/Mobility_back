from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:1234@localhost:13306/mobility")
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()