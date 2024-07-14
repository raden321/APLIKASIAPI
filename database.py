from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# ahyar diganti dengan username mysql/phpmyadmin
# bismillah1 diganti dengan passwordnya
# ApiAplication diganti dengan nama databasenya
URL_DATABASE = "mysql+pymysql://uarqvaj7pairfte0:dF1fNuTI6BJkFcvTgak3@buewulu9b7imhll3mi9u-mysql.services.clever-cloud.com:3306/buewulu9b7imhll3mi9u"



engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
