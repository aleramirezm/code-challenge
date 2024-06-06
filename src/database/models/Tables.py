from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import declarative_base


Base = declarative_base()

def get_base():
    return Base

class Product(Base):
    """Python representation of a MYSQL Table"""
    __tablename__="Product"
    id = Column(String(36), primary_key=True)
    category = Column(String(36))
    capacity = Column(Float)
    color = Column(String(36))
    screen_size = Column(String(36))
    memory = Column(String(36))
    other_specs = Column(String(100))

class Sales(Base):
    """Python representation of a MYSQL Table"""
    __tablename__="Sales"
    product_id = Column(String(36), primary_key=True) # not an actual primary key, but a foreign key.
    country = Column(String(36))
    price = Column(Float)
    quantity = Column(Float)
    final_sales = Column(Integer)
    
class TransformedSales(Base):
    __tablename__="TransformedSales"
    id = Column(String(36), primary_key=True) # not an actual primary key, but a foreign key.
    country = Column(String(36))
    revenue = Column(Float)
    category = Column(String(36))
    sales_volume = Column(String(20))    
    