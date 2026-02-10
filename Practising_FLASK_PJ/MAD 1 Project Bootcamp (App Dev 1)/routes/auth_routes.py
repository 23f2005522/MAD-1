from flask import Blueprint , render_template, request, session , flash , redirect , url_for
from db.db import db
from models.models import User , Role , UserRole


auth_bp = Blueprint("auth" , __name__)

@auth_bp.route("/login", methods=["GET" , "POST"])
def login():
    if request.method == "GET":
        # if already logged in Redirect to dashboard
        if "user_email" in session:
            print("aa")
            return render_template("home.html")
        return render_template("login.html")
    

    if request.method == "POST":
        email = request.form.get("email" , None)
        password = request.form.get("password" , None)
        
        #Data Validation
        if(not email or not password):
            flash("Email and Password are required!" , "error")
            return render_template("login.html")
        
        if not ("@" in email and "." in email):
            flash("Invalid email format!" , "error")
            return render_template("login.html")
        
        if len(password) < 6 or len(password) > 20:
            flash("Password must be at least 6 characters long!" , "error")
            return render_template("login.html")
        
        
        # Logic to authenticate user
        user = User.query.filter_by(email=email , password=password).first()
        if not user:
            flash("Invalid email or password!" , "error")
            return render_template("login.html")
        
        if user.password != password:
            flash("Incorrect password!" , "error")
            return render_template("login.html")
        
        
        # Set session variables
        session["user_email"] = user.email
        session["user_role"] = [ role.name for role in user.roles]
        flash("Login successful!" , "success")
        
        #Redirect to homepage
        return render_template("home.html")
        
        
@auth_bp.route("/logout" , methods=["GET"])
def logout(): 
    if "user_email" not in session:
        flash("You are not logged in!" , "error")
        return redirect(url_for("auth.login"))

    session.pop("user_email" , None)
    session.pop("user_role" , None)
    flash("Logged out successfully!" , "success")
    
    return redirect(url_for("auth.login"))


@auth_bp.route("/register", methods=["GET", "POST"])
def Register():
    if request.method == "GET":
        return render_template("register.html")

    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    confirm_password = request.form.get("confirm_password")
    role_name = request.form.get("role")

    # 1️⃣ Validation
    if not name or not email or not password or not confirm_password or not role_name:
        flash("All fields are required!", "error")
        return render_template("register.html")

    if "@" not in email or "." not in email:
        flash("Invalid email format!", "error")
        return render_template("register.html")

    if len(password) < 6 or len(password) > 20:
        flash("Password must be between 6 and 20 characters!", "error")
        return render_template("register.html")

    if password != confirm_password:
        flash("Passwords do not match!", "error")
        return render_template("register.html")

    if role_name not in ["customer", "store_manager"]:
        flash("Invalid role selected!", "error")
        return render_template("register.html")

    # 2️⃣ Existing user check
    if User.query.filter_by(email=email).first():
        flash("Email already registered!", "error")
        return render_template("register.html")

    # 3️⃣ Fetch role
    role = Role.query.filter_by(name=role_name).first()

    # 4️⃣ Create user (relationship handles user_role)
    new_user = User(
        name=name,
        email=email,
        password=password,   # later → hash
        roles=[role]
    )

    db.session.add(new_user)
    db.session.commit()   # ✅ user_id now exists

    flash("Registration successful! Please log in.", "success")
    return redirect(url_for("auth.login"))



        
        
        
        