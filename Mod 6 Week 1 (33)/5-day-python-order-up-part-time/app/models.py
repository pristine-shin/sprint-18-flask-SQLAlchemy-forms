from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


class Employee(db.Model, UserMixin):
    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model):
    __tablename__ = "menus"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    items = relationship("MenuItem", back_populates="menu")


class MenuItem(db.Model):
    __tablename__ = "menu_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, ForeignKey("menus.id"), nullable=False)
    menu_type_id = db.Column(db.Integer, ForeignKey("menu_item_types.id"), nullable=False)

    menu = relationship("Menu", back_populates='items')
    menu_item_type = relationship("MenuItemType", back_populates='menu_items')


class MenuItemType(db.Model):
    __tablename__ = "menu_item_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

    menu_items = relationship("MenuItem", back_populates='menu_item_type')


class Table(db.Model):
    __tablename__ = "tables"

    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
