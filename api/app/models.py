from app.database import Base
import sqlalchemy as sql

class Course(Base):
    __tablename__ = "courses"

    id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String)
    price = sql.Column(sql.Float)