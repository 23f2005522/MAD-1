import os
from random import randint
from flask import Blueprint, render_template, request , flash , session , current_app
from db.db import db

from models.models import Product , Category


add_product_bp = Blueprint("add_product" , __name__)

@add_product_bp.route("/add_product" , methods=["GET" , "POST"])
def add_product():
    if request.method == "GET":
        return render_template("add_products.html" , categories = Category.query.all())
    
    if request.method == "POST":
        print(request.form)
        # #files 
        # print(request.files.get("document") , "file")
        
        
        
        if "store_manager"  in session.get("user_role" , []):
        
            # Get category name and description from form
            name = request.form.get("name" , None)
            description = request.form.get("description" , None)
            price = request.form.get("price" , None)
            category_id = request.form.get("category_id" , None)
            product_file = request.files.get("document" , None)
        
            # Data validation
            if not name or name.strip() == "" :
                flash("Product name is required!" , "error")
                return render_template("add_products.html" , error = "Product name is required!")
            
            if not price or price.strip() == "" :
                flash("Product price is required!" , "error")
                return render_template("add_products.html" , error = "Product price is required!")
            
            try:
                price = float(price)
                if price < 0:
                    raise ValueError
            except ValueError:
                flash("Invalid price! Price must be a positive number." , "error")
                return render_template("add_products.html" , error = "Invalid price! Price must be a positive number.")
            
            # write the file to disk and get the url to save in db
            file_url = None
            if product_file:
                filename = f"{product_file.filename.split('.')[0]}_{randint(1000,9999)}.{product_file.filename.split('.')[-1]}"
                file_path = os.path.join(
                    current_app.config["UPLOAD_FOLDER"],
                    filename
                )
                product_file.save(file_path)
                file_url = file_path
            
            
            # if catergory with same name already exists dont creat a new one and not present dont create the product
            print(category_id , "category id")
            exsisting_category = Category.query.filter_by(id = category_id).first()
            if not exsisting_category:
                flash("Category does not exist!" , "error")
                return render_template("add_products.html" , error = "Category does not exist!")
            
            
            # Create and save the new category
            product = Product(name = name , description = description, price=price, Category_id=category_id, product_details_url=file_url)
            if not product : 
                flash("Error creating product!" , "error")
                return render_template("add_products.html" , error = "Error creating product!")
            db.session.add(product)
            db.session.commit()
            
            
            flash("Product added successfully!" , "success")
            return render_template("home.html" , success = "Product added successfully!")
        
        
        else  : 
            flash("You are not authorized to add products!" , "error")
            return render_template("home.html")