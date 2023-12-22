from peewee import Model, CharField, IntegerField, FloatField, ForeignKeyField
from peewee import *  
import settings


db = SqliteDatabase(database=f'{settings.DATABASE_PATH}/{settings.DATABASE_NAME}')

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    position = CharField(default='')
    login = CharField(default='')
    password = CharField(default='')
    power_level = IntegerField(default=0)

class Customer(BaseModel):
    name = CharField(default='')
    address = CharField(default='')
    phone = CharField(default='')

class Product(BaseModel):
    name = CharField(default='')
    description = TextField(default='')
    price = FloatField(default=0)
    quantity = IntegerField(default=0)

class Order(BaseModel):
    customer_id = ForeignKeyField(Customer, backref='orders', default=0)
    order_date = TextField(default='')
    total_amount = FloatField(default=0)

class OrderItem(BaseModel):
    order_id = ForeignKeyField(Order, backref='order_items', default=0)
    product_id = ForeignKeyField(Product, backref='order_items', default=0)
    quantity = IntegerField(default=0)
    price = FloatField(default=0)

class Supplier(BaseModel):
    name = CharField(default='')
    address = CharField(default='')
    phone = CharField(default='')

db.create_tables([User, Customer, Product, Order, OrderItem, Supplier])