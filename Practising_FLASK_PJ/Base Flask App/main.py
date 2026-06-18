from flask import Flask
from db.db import db  
from config.config import Config
# import the models before they are creating database tables inside the app context 
from model.model import * 
# importing Routes Here
from routes.home_route import home_bp




#creating app
app = Flask(__name__, template_folder="templates", static_folder="static") 
# configuration of using Config class from config.py
app.config.from_object(Config) 
db.init_app(app) 



#AutoCreation DB_tables and Admin if not present
with app.app_context() :  #  temporarily make this Flask app the active app so Flask-related operations can run.
    db.create_all()  ## Create the database tables if they don't exist and if they exist then it will not create again
    
     
    # db comes from Flask-SQLAlchemy, not plain SQLAlchemy.
    # So db needs Flask app information to know things like:
    #                     which database URL to use
    #                     which engine/session belongs to the current app
    #                     which config values are set
    
    ####    Use with app.app_context(): whenever your code is running outside a request, but still needs Flask app-bound things.
        # 1. Creating tables at startup
        # 2. Seeding initial data
        #                 if not RoleModel.query.filter_by(name="admin").first():
        #                         db.session.add(Role(name="admin"))
        #                         db.session.commit()

   



#registering the All routes to the APP here
app.register_blueprint(home_bp)


    
    
    
    

if (__name__ == "__main__") :
    app.run(debug = True) 
    