from flask import Blueprint, render_template, request , flash , session
from db.db import db
from models.models import Category


add_category_bp = Blueprint("add_category" , __name__)


@add_category_bp.route("/add_category" , methods=["GET" , "POST"])
def add_category():
    if request.method == "GET":
        return render_template("add_category.html")
    
    if request.method == "POST":
        
        if "admin"  in session.get("user_role" , []):
        
            # Get category name and description from form
            name = request.form.get("name" , None)
            description = request.form.get("description" , None)
        
            # Data validation
            if not name or name.strip() == "" :
                flash("Category name is required!" , "error")
                return render_template("add_category.html" , error = "Category name is required!")
            
            # if catergory with same name already exists dont creat a new one
            exsisting_category = Category.query.filter_by(name = name).first()
            if exsisting_category:
                flash("Category already exists!" , "error")
                return render_template("add_category.html" , error = "Category already exists!")
            
            
            # Create and save the new category
            category = Category(name = name , description = description)
            db.session.add(category)
            db.session.commit()
            
            
            flash("Category added successfully!" , "success")
            return render_template("home.html" , success = "Category added successfully!")
        
        
        else  : 
            flash("You are not authorized to add categories!" , "error")
            return render_template("home.html")