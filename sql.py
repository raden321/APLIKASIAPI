from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

# Update dengan detail koneksi MySQL Anda
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:@localhost:3306/ApiAplication"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

# Tambahkan 5 data
users = [
    {"username": "alice"},
    {"username": "bob"},
    {"username": "charlie"},
    {"username": "david"},
    {"username": "eve"}
]

for user in users:
    db_user = models.User(**user)
    db.add(db_user)

db.commit()
db.close()
