# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#engine = create_engine('sqlite:////home/veronika/PycharmProjects/training/task5/test2.db', echo = True)
#engine = create_engine('postgresql+psycopg2://postgres:q1@localhost/', echo = True)
#engine = create_engine('mysql+mysqldb://root:q1@localhost/prodaction', echo = True)

Base = declarative_base()


class Factory(Base):
    __tablename__ = 'factory'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    product = relationship("Product", backref="factory",
                             order_by="Product.id")


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(String)

    customer = relationship("Customer", backref='product',
                            order_by="Customer.id")

    factory_id = Column(ForeignKey('factory.id'))


class Customer(Base):
    __tablename__ = 'customer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)

    product_id = Column(ForeignKey('product.id'))


Base.metadata.create_all(engine)