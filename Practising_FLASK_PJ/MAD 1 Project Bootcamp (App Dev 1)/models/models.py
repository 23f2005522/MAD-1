from db.db import db


class Role(db.Model):
    __tablename__ = "role"

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class User(db.Model):
    __tablename__ = "user"

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    roles = db.relationship("Role" , secondary="user_role", backref="users" )
    customers_details = db.relationship("Customer" , backref = "user" , lazy = True )
    store_managers_details = db.relationship("StoreManager" , backref = "user" , lazy = True , uselist = False)
    

class UserRole(db.Model):
    __tablename__ = "user_role"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("role.role_id"), nullable=False)


class StoreManager(db.Model):
    __tablename__ = "store_manager"

    manager_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    store_name = db.Column(db.String(100), nullable=False)
    qualification = db.Column(db.String(200), nullable=True)


class Customer(db.Model):
    __tablename__ = "customer"

    customer_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    preferred_mode_of_payment = db.Column(db.String(50), nullable=True)



class Category(db.Model): 
    __tablename__ = "category"
    
    id = db.Column(db.Integer , primary_key = True , autoincrement =True )
    name = db.Column(db.String(100) , unique = True , nullable = False)
    description = db.Column(db.String(200) , nullable = True)
    products = db.relationship("Product" , backref = "category" , lazy = True)
    
    
class Product(db.Model):
    __tablename__ = "product"
    
    id = db.Column(db.Integer , primary_key = True , autoincrement = True)
    name = db.Column(db.String(100) , nullable = False)
    description = db.Column(db.String(200) , nullable = True)
    price = db.Column(db.Float , nullable = False)
    product_details_url = db.Column(db.String(200) , nullable = True)
    Category_id  = db.Column(db.Integer , db.ForeignKey("category.id") , nullable = False)