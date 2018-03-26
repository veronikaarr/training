# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from operator import itemgetter
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

"""ДобавЬте данных (демо данных) и сделайте выборку как то
найти всех производителей у которых более 2 товаров по цене 10 долларов и ниже."""

'''q = session.execute("CREATE VIEW prod(f_name, p_numb)"
                    " AS SELECT f_name, COUNT(p_id) FROM product JOIN factory ON product.factory_id = factory.f_id"
                    " WHERE product.price <= 10 GROUP BY f_id;"
                    " SELECT f_name FROM prod"
                    " WHERE p_numb = 2;")'''

"""Найти всех покупателей которые делали заказы и сгрупировать их по компаниям производителям чьи товары покупались"""

'''q1 = session.execute("SELECT c_name, f_name FROM customer JOIN product ON customer.product_id = product.p_id"
                    " JOIN factory on product.factory_id = factory.f_id ORDER BY f_id;")'''

"""Найти самые популярные товары у каждого производителя и указать сколько таких товаров было куплено. <Недоделано>"""
'''q2 = session.execute("CREATE VIEW prod(f_name, p_name, p_numb) AS"
                     " SELECT f_name, p_name, COUNT(p_name) FROM customer JOIN product ON customer.product_id = "
                     " product.p_id JOIN factory ON product.factory_id = factory.f_id GROUP BY p_id; "
                     " SELECT o.* FROM prod o "
                     " LEFT JOIN prod b ON o.f_name = b.f_name AND o.p_numb < b.p_numb"
                     " WHERE b.p_numb is NULL;")'''

"""Найти всех производителей товаров которые продавались с указанием их выручек по каждому виду товара и те которые 
еще не продавались"""
q3 = session.execute("SELECT p_name, SUM(price), product_id, f_name FROM product LEFT JOIN customer ON "
                     " customer.product_id = product.p_id JOIN factory ON product.factory_id = factory.f_id "
                     " GROUP BY p_id;")

#res = q2.fetchall()
sales = q3.fetchall()

for i in range(0,len(sales)):
    if (itemgetter(2)(sales[i]) is None):
        print("The{} is not sold".format(itemgetter(0)(sales[i])))
    else:
        print(sales[i])
session.commit()
#print(res)

Base.metadata.create_all(engine)