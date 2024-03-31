from sqlalchemy import Column, String, Integer, DateTime, Date, Float,ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
# Таблица пользователя
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    city = Column(String)
    reg_date = Column(DateTime)
    purchase = Column(String, ForeignKey('cars.car_id'))
    purchase_fk = relationship('Car',foreign_keys=[purchase],  lazy='subquery')
    sale = Column(String, ForeignKey('cars.car_id'))
    sale_fk = relationship('Car', foreign_keys=[sale], lazy='subquery')
    password = Column(Integer)
# Таблица category
class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True, autoincrement=True)
    category = Column(String)
    name = Column(String,ForeignKey('cars.car_id'))
    name_fk = relationship('Car',foreign_keys=[name], lazy='subquery')
# Таблица задач
class Car(Base):
    __tablename__ = 'cars'
    mark = Column(Integer)
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    model = Column(Integer)
    cost = Column(Text)
    status = Column(String)
    user_id = Column(String, ForeignKey('users.user_id'))
    category = Column(String,ForeignKey('category.category'))
    name = Column(String)
    host_id = Column(Integer)
    user_id_fk = relationship('User',foreign_keys=[user_id],lazy='subquery')
    category_id_fk = relationship('Category', foreign_keys=[category], lazy='subquery')
# Таблица комм
class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(Integer, ForeignKey('users.user_id'))
    post_id = Column(Integer, ForeignKey('cars.car_id'))
    comment_text = Column(Text)
    publish_date = Column(DateTime)
    user_fk = relationship(User,foreign_keys=[userid], lazy='subquery')
    post_fk = relationship(Car,foreign_keys=[post_id], lazy='subquery')



