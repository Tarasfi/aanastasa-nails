from db import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class Price(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)  
    price: Mapped[str] = mapped_column(String(250), nullable=True)     
    service_type: Mapped[str] = mapped_column(String(250), nullable=True)