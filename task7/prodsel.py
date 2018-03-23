# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

#engine = create_engine('sqlite:////home/veronika/PycharmProjects/training/task5/test2.db', echo = True)
#engine = create_engine('postgresql+psycopg2://postgres:q1@localhost/', echo = True)
engine = create_engine('mysql+mysqldb://root:q1@localhost/prodaction', echo = True)

Base = declarative_base()


class Factory(Base):
    __tablename__ = 'factory'
    f_id = Column(Integer, primary_key=True, autoincrement=True)
    f_name = Column(String(32))

    product = relationship("Product", backref="factory",
                             order_by="Product.p_id")


class Customer(Base):
    __tablename__ = 'customer'

    c_id = Column(Integer, primary_key=True, autoincrement=True)
    c_name = Column(String(32))

    product_id = Column(ForeignKey('product.p_id'))


class Product(Base):
    __tablename__ = 'product'
    p_id = Column(Integer, primary_key=True, autoincrement=True)
    p_name = Column(String(32))
    price = Column(Integer)

    customer = relationship("Customer", backref='product',
                            order_by="Customer.c_id")

    factory_id = Column(ForeignKey('factory.f_id'))

Session = sessionmaker(bind=engine)
conn = engine.connect()
session = Session(bind=conn)

#q = session.execute(func.count(Customer.id))
"""ДобавЬте данных (демо данных) и сделайте выборку как то
найти всех производителей у которых более 2 товаров по цене 10 долларов и ниже."""

q = session.execute("CREATE VIEW prod(f_name, p_numb)"
                    " AS SELECT f_name, COUNT(p_id) FROM product JOIN factory ON product.factory_id = factory.f_id"
                    " WHERE product.price <= 10 GROUP BY f_id;"
                    " SELECT f_name FROM prod"
                    " WHERE p_numb = 2;")

"""Найти всех покупателей которые делали заказы и сгрупировать их по компаниям производителям чьи товары покупались"""

q1 = session.execute("SELECT c_name, f_name FROM customer JOIN product ON customer.product_id = product.p_id"
                    " JOIN factory on product.factory_id = factory.f_id ORDER BY f_id;")

"""Найти самые популярные товары у каждого производителя и указать сколько таких товаров было куплено. <Недоделано>"""
q2 = session.execute("CREATE VIEW popular(f_name, p_name) AS"
                    " SELECT f_name, p_name FROM customer JOIN product ON customer.product_id = product.p_id"
                    " JOIN factory on product.factory_id = factory.f_id;"
                    " SELECT p_name, COUNT(*) FROM popular GROUP BY p_name;")

session.commit()
print(q)

Base.metadata.create_all(engine)