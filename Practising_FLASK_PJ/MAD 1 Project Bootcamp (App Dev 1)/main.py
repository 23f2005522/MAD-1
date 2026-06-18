from flask import Flask,
from db.db import db
from config.config import Config
from models.models import *
from routes.auth_routes import auth_bp
from routes.home_route import home_bp
from routes.add_category import add_category_bp
from routes.add_product import add_product_bp


app = Flask(__name__, template_folder="templates", static_folder="static")

app.config.from_object(Config)
db.init_app(app) 


with app.app_context():
    # 1️⃣ Create tables
    db.create_all()

    # 2️⃣ Create roles if not exists
    roles = ["admin", "customer", "store_manager"]

    for role_name in roles:
        role = Role.query.filter_by(name=role_name).first()
        if not role:
            db.session.add(Role(name=role_name))

    db.session.commit()

    # 3️⃣ Create Super Admin user
    admin_user = User.query.filter_by(email="admin@gmail.com").first()

    if not admin_user:
        
        admin_role_id = Role.query.filter_by(name="admin").first()
        StoreManager_role_id = Role.query.filter_by(name="store_manager").first()
        admin_user = User(
            name="Super_Admin",
            email="admin@gmail.com",
            password="admin",
            roles=[admin_role_id , StoreManager_role_id]
        )
        db.session.add(admin_user)
        db.session.commit()  # user_id generated here

        # 4️⃣ Assigning user<-->role to Super Admin
        user_role = UserRole(
            user_id = admin_user.user_id,
            role_id = admin_role_id
        )





app.register_blueprint(home_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(add_category_bp)
app.register_blueprint(add_product_bp)

if __name__ == "__main__":
    app.run(debug=True)
