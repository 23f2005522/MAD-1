class Config : 
    SQLALCHEMY_DATABASE_URI  = "sqlite:///databse.sqlite3"
    SECRET_KEY = "supersecretkey"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = "static/uploads"