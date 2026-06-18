from flask import Flask,render_template,request,redirect,url_for 


app = Flask(__name__) # __name__ : it is a special variable in Python that holds the name of the module in which it is used.

@app.route('/') # binds the URL '/' to the hello_world function so when a user accesses this URL, the function is executed.
def hello_world():
    return 'hi !'  
# when a user accesses the root URL, the hello_world function is called, and it returns 'Hello, World!'

# by default, app.route() responds to GET requests. If you want to handle other HTTP methods (like POST, PUT, DELETE), you can specify them using the methods parameter in the route decorator.
# Example: @app.route('/submit', methods=['POST'])
# def submit():
#     return 'Form Submitted!'
# This would handle POST requests to the /submit URL.


# defination name for the function for each route should be unique. other wise it will give an error known as "View function mapping is overwriting an existing endpoint function".


@app.route('/greet')
def greet():
    return "<h1>Welcome to Flask!</h1>" 


# bindind multiple routes to the same function
@app.route('/welcome')
@app.route('/welcome2')
@app.route('/welcome3')
def welcome():
    return "<h1>Welcome to Flask!</h1>"

 



# use external HTML file use flask to render it using render_template function and render_template function looks for HTML files in a folder named templates by default. to bypass this default behavior, you can specify a different folder by providing the template_folder parameter when creating the Flask app instance.
# Example: app = Flask(__name__, template_folder='my_templates')
@app.route('/course')
def course():
    return render_template('course.html')


### Dynamic Routing : Dynamic routing allows you to create routes that can accept variable parts in the URL. these variable parts are specified using angle brackets <> in the route definition. when a user accesses a URL that matches the dynamic route, the variable part is extracted and passed as an argument to the associated view function.
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'





## one route post and get method
@app.route('/form' , methods = ['GET','POST'])
def form():
    if (request.method == "GET") : 
        return render_template('form.html')
    if ( request.method == "POST") : 
        # process the form data
        
        print(request)
        print(request.form["name"] , request.form["email"] , request.form.get("name")) # form is a dictionary-like object that contains the key-value pairs of form data submitted in the request body.
        
        ### why i cant access itr . notation  like request.form.name ? 
        
        ### because form is a MultiDict (a special type of dictionary) that does not support dot notation for accessing keys.
        
        ### get method is used to access the value associated with a specific key in the MultiDict. it returns None if the key does not exist instead of raising a KeyError.   
        
        #### MultiDict ? 
        """
            ✅ What is a MultiDict?

                A MultiDict works like:

                d = MultiDict()
                d.add("color", "red")
                d.add("color", "blue")


                Now the key "color" maps to both "red" and "blue".

                In a normal Python dict:

                d["color"] = "red"
                d["color"] = "blue"  # overwrites old value


                Normal dicts overwrite keys → MultiDict stores all values.  

                
                
                Examples from web development:
                        1. Query parameters : A query parameter is a key-value pair added to the end of a URL to pass information to a web server. Query parameters begin after a ? and multiple parameters are separated by &.

                        URL:

                        /search?tag=python&tag=ai&tag=ml


                        Here tag appears three times.
                        A normal dict cannot store all three values, but a MultiDict can:

                        request.args.getlist("tag")
                        # ["python", "ai", "ml"]

                        2. HTML form fields

                        Checkboxes:

                        <input type="checkbox" name="skills" value="python">
                        <input type="checkbox" name="skills" value="ml">
                        <input type="checkbox" name="skills" value="dl">


                        The user may select multiple values → MultiDict required.
        
        """
        
        # MultiDict is a specialized data structure provided by the Werkzeug library, which is used by Flask to handle form data and query parameters in HTTP requests. Unlike a standard dictionary, a MultiDict can store multiple values for the same key. This is particularly useful for handling form submissions where multiple form fields may share the same name (e.g., checkboxes or multi-select dropdowns).
                
            
       
        return render_template('user.html' , name = request.form["name"] , email = request.form["email"] )

## request is imported from flask module which is used to handle incoming request data in Flask applications. It is a object that provides access to various attributes and methods related to the current HTTP request being processed by the Flask application. for example, you can use request to access form data, query parameters, headers, and more. 

    # req form browser comes   --> flasK --> request object --> access the data using request object which also contains .form --> multiDict --> key value pairs of form data


## if we submit data using get method it we will come to backend as search query parameters in the URL. for example, if we submit a form with a field named username and the value "john", the URL will look like this: http://example.com/form?username=john
# @app.route('/search', methods = ['GET'])
# def search():
#     if (request.method == "GET") : 
#         print(request)
#         print(request.args)
#           ########## args is a dictionary-like object that contains the key-value pairs of query parameters sent in the URL.
#         return "Search Completed"


## if we submit data using post method it will not be visible in the URL. instead, it will be sent in the body of the HTTP request. this is more secure for sensitive data like passwords.



## redirecting to another route
@app.route('/redirect')
def redirect_to_random():
    return redirect("/greet")



# url_for() :  is a function in Flask that is used to generate URLs for specific routes defined in the application. it is useful for creating dynamic links within your application, as it allows you to reference routes by their function names rather than hardcoding URLs. this helps to maintain consistency and makes it easier to change URLs if needed.
#### argument : function name  returns : the URL associated with that function.
### example : url_for('greet') will return '/greet' if the greet function

@app.route('/redirect2') 
def x() : 
    return redirect(url_for('greet'))


## 404 error handling
@app.errorhandler(404)
def page_not_found(e): #3 e is the error object that contains information about the error that occurred.
    return render_template('404.html'), 404



app.run(debug=True)
# debug mode: When you run a Flask application in debug mode, it provides helpful error messages and automatically reloads the server when code changes are detected. This is useful during development but should be turned off in production for security reasons.


"""
===============================================================================
                        DETAILED QUICK REFERENCE CHEAT SHEET
===============================================================================

┌─────────────────────────────────────────────────────────────────────────────┐
│ FLASK APPLICATION SETUP                                                     │
└─────────────────────────────────────────────────────────────────────────────┘

from flask import Flask, render_template, request, redirect, url_for, flash, 
                  session, jsonify, abort, make_response

# Basic Setup
app = Flask(__name__)                              # Create Flask app
app = Flask(__name__, template_folder='templates') # Custom template folder
app = Flask(__name__, static_folder='static')      # Custom static folder
app.secret_key = 'your-secret-key'                 # Required for sessions/flash
app.config['DEBUG'] = True                         # Enable debug mode

# Running the App
app.run()                                          # Default: localhost:5000
app.run(debug=True)                                # With debug mode
app.run(host='0.0.0.0', port=8080)                # Custom host and port
app.run(threaded=True)                             # Enable threading

┌─────────────────────────────────────────────────────────────────────────────┐
│ ROUTING & URL RULES                                                         │
└─────────────────────────────────────────────────────────────────────────────┘

# Basic Routes
@app.route('/')                                    # Root URL
@app.route('/about')                               # Static route
@app.route('/home', endpoint='homepage')           # Custom endpoint name

# Multiple Routes
@app.route('/welcome')                             # Multiple URLs to same
@app.route('/greet')                               # function
def welcome():
    return "Welcome!"

# HTTP Methods
@app.route('/data', methods=['GET'])               # GET only (default)
@app.route('/submit', methods=['POST'])            # POST only
@app.route('/form', methods=['GET', 'POST'])       # Multiple methods
@app.route('/api', methods=['GET', 'POST', 'PUT', 'DELETE'])  # REST API

# Dynamic Routes (URL Parameters)
@app.route('/user/<username>')                     # String (default)
@app.route('/post/<int:post_id>')                  # Integer
@app.route('/price/<float:amount>')                # Float
@app.route('/page/<path:subpath>')                 # Path with slashes
@app.route('/uuid/<uuid:identifier>')              # UUID format

# Multiple Parameters
@app.route('/user/<username>/post/<int:post_id>')
def show_user_post(username, post_id):
    return f'{username}: {post_id}'

# Optional URL Parts
@app.route('/blog/')                               # Trailing slash
@app.route('/blog')                                # No trailing slash

┌─────────────────────────────────────────────────────────────────────────────┐
│ REQUEST OBJECT - ACCESSING DATA                                            │
└─────────────────────────────────────────────────────────────────────────────┘

# HTTP Method
request.method                                     # 'GET', 'POST', 'PUT', etc.

# Form Data (POST requests)
request.form['name']                               # Get value (raises KeyError)
request.form.get('name')                           # Get value (returns None)
request.form.get('name', 'default')                # With default value
request.form.getlist('hobbies')                    # Multiple values (list)
request.form.to_dict()                             # Convert to dict

# Query Parameters (GET requests - URL ?key=value)
request.args.get('search')                         # Get query param
request.args.get('page', 1, type=int)              # With type conversion
request.args.getlist('tags')                       # Multiple values
request.args.to_dict()                             # All params as dict

# JSON Data
request.json                                       # Auto-parsed JSON
request.get_json()                                 # Same as above
request.get_json(force=True)                       # Force JSON parsing
request.is_json                                    # Check if request is JSON

# File Uploads
request.files['photo']                             # Get uploaded file
request.files.get('photo')                         # Safe get
file = request.files['photo']
file.filename                                      # Original filename
file.save('/path/to/save')                         # Save file
file.read()                                        # Read file content

# Headers
request.headers.get('User-Agent')                  # Get specific header
request.headers.get('Content-Type')
dict(request.headers)                              # All headers as dict

# Cookies
request.cookies.get('session_id')                  # Get cookie value
request.cookies.get('user', 'guest')               # With default

# URL & Path Info
request.url                                        # Full URL
request.base_url                                   # URL without query string
request.path                                       # Path only (/user/123)
request.host                                       # Hostname (example.com)
request.scheme                                     # http or https
request.endpoint                                   # Function endpoint name

# Request Data
request.data                                       # Raw request body
request.values                                     # Combined form + args
request.content_length                             # Request body size
request.content_type                               # Content type header

# Client Info
request.remote_addr                                # Client IP address
request.referrer                                   # Referring URL
request.user_agent                                 # User agent object

┌─────────────────────────────────────────────────────────────────────────────┐
│ RESPONSES & RETURN VALUES                                                  │
└─────────────────────────────────────────────────────────────────────────────┘

# Simple Returns
return 'Hello World'                               # Plain text (200)
return '<h1>Title</h1>'                            # HTML string
return 'Error', 400                                # With status code
return 'Not Found', 404, {'X-Custom': 'value'}     # With headers

# Template Rendering
return render_template('index.html')               # Render template
return render_template('page.html', title='Home') # Pass variables
return render_template('list.html', items=items)  # Pass lists/dicts

# JSON Responses
return jsonify({'key': 'value'})                   # JSON response
return jsonify(name='John', age=30)                # Keyword arguments
return jsonify([1, 2, 3])                          # List to JSON
return jsonify({'status': 'ok'}), 201              # With status code

# Redirects
return redirect('/home')                           # Redirect to URL
return redirect(url_for('home'))                   # Using url_for
return redirect('https://google.com')              # External redirect
return redirect('/login', code=301)                # Permanent redirect

# Custom Response Object
from flask import make_response
response = make_response('Hello')                  # Create response
response.status_code = 200                         # Set status
response.headers['X-Custom'] = 'value'             # Set headers
response.set_cookie('name', 'value')               # Set cookie
return response

# File Downloads
from flask import send_file, send_from_directory
return send_file('path/to/file.pdf')               # Send file
return send_file('image.jpg', mimetype='image/jpeg')
return send_from_directory('uploads', 'file.pdf')  # From directory

# Error Responses
abort(404)                                         # 404 Not Found
abort(403)                                         # 403 Forbidden
abort(500)                                         # 500 Internal Error
abort(401)                                         # 401 Unauthorized

┌─────────────────────────────────────────────────────────────────────────────┐
│ URL BUILDING & NAVIGATION                                                  │
└─────────────────────────────────────────────────────────────────────────────┘

# url_for() Function
url_for('home')                                    # Generate URL for route
url_for('show_user', username='john')              # With parameters
url_for('search', q='flask', page=1)               # With query params
url_for('static', filename='style.css')            # Static files
url_for('home', _external=True)                    # Absolute URL
url_for('home', _scheme='https')                   # Force HTTPS
url_for('home', _anchor='section1')                # Add #anchor

# Redirect with url_for
return redirect(url_for('login'))                  # Redirect to function
return redirect(url_for('profile', user_id=123))   # With parameters

┌─────────────────────────────────────────────────────────────────────────────┐
│ TEMPLATES (JINJA2)                                                         │
└─────────────────────────────────────────────────────────────────────────────┘

# Variables
{{ variable }}                                     # Print variable
{{ user.name }}                                    # Object attribute
{{ user['name'] }}                                 # Dictionary key
{{ items[0] }}                                     # List index

# Control Structures
{% if condition %}                                 # If statement
    <p>True</p>
{% elif other_condition %}
    <p>Other</p>
{% else %}
    <p>False</p>
{% endif %}

{% for item in items %}                            # For loop
    <li>{{ item }}</li>
{% endfor %}

{% for key, value in dict.items() %}               # Dict iteration
    {{ key }}: {{ value }}
{% endfor %}

{% for i in range(5) %}                            # Range loop
    {{ i }}
{% endfor %}

# Loop Variables
{% for item in items %}
    {{ loop.index }}                               # Current iteration (1-indexed)
    {{ loop.index0 }}                              # Current iteration (0-indexed)
    {{ loop.first }}                               # First iteration? (boolean)
    {{ loop.last }}                                # Last iteration? (boolean)
    {{ loop.length }}                              # Total items
{% endfor %}

# Filters
{{ name|upper }}                                   # Uppercase
{{ name|lower }}                                   # Lowercase
{{ name|title }}                                   # Title Case
{{ text|truncate(20) }}                            # Truncate to 20 chars
{{ price|round(2) }}                               # Round to 2 decimals
{{ items|length }}                                 # Length
{{ items|join(', ') }}                             # Join list
{{ html|safe }}                                    # Mark as safe HTML
{{ text|escape }}                                  # Escape HTML
{{ date|date('%Y-%m-%d') }}                        # Format date
{{ value|default('N/A') }}                         # Default value

# Template Inheritance
{% extends "base.html" %}                          # Extend base template

{% block title %}Page Title{% endblock %}          # Define block

{% block content %}                                # Override block
    <h1>Content</h1>
{% endblock %}

# Include Templates
{% include 'header.html' %}                        # Include template

# Comments
{# This is a comment #}                            # Single line
{% comment %}                                      # Multi-line
    This is a comment
{% endcomment %}

# URL Generation
<a href="{{ url_for('home') }}">Home</a>           # Generate URL
<a href="{{ url_for('profile', user='john') }}">Profile</a>

# Static Files
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
<script src="{{ url_for('static', filename='script.js') }}"></script>
<img src="{{ url_for('static', filename='logo.png') }}">

┌─────────────────────────────────────────────────────────────────────────────┐
│ ERROR HANDLING                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

# Custom Error Handlers
@app.errorhandler(404)                             # 404 Not Found
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)                             # 500 Server Error
def server_error(error):
    return render_template('500.html'), 500

@app.errorhandler(403)                             # 403 Forbidden
def forbidden(error):
    return 'Forbidden', 403

@app.errorhandler(Exception)                       # All exceptions
def handle_exception(error):
    return 'An error occurred', 500

# Trigger Errors
abort(404)                                         # Raise 404
abort(403, 'Access denied')                        # With description

┌─────────────────────────────────────────────────────────────────────────────┐
│ SESSION MANAGEMENT                                                          │
└─────────────────────────────────────────────────────────────────────────────┘

# Session (requires app.secret_key)
session['username'] = 'john'                       # Set session variable
username = session.get('username')                 # Get session variable
session.pop('username', None)                      # Remove from session
session.clear()                                    # Clear all session data
'username' in session                              # Check if key exists

# Session Configuration
app.config['SESSION_COOKIE_NAME'] = 'my_session'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True         # HTTPS only
app.config['PERMANENT_SESSION_LIFETIME'] = 3600    # Seconds

┌─────────────────────────────────────────────────────────────────────────────┐
│ FLASH MESSAGES                                                              │
└─────────────────────────────────────────────────────────────────────────────┘

# Flash Messages (requires app.secret_key)
flash('Success message')                           # Add flash message
flash('Error occurred', 'error')                   # With category
flash('Warning!', 'warning')
flash('Info message', 'info')

# In Template
{% with messages = get_flashed_messages() %}
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
{% endwith %}

# With Categories
{% with messages = get_flashed_messages(with_categories=true) %}
    {% for category, message in messages %}
        <div class="{{ category }}">{{ message }}</div>
    {% endfor %}
{% endwith %}

┌─────────────────────────────────────────────────────────────────────────────┐
│ COOKIES                                                                     │
└─────────────────────────────────────────────────────────────────────────────┘

# Set Cookie
resp = make_response('Hello')
resp.set_cookie('username', 'john')                # Set cookie
resp.set_cookie('id', '123', max_age=3600)         # Expires in 1 hour
resp.set_cookie('token', 'abc', httponly=True)     # HTTP only
resp.set_cookie('secure', 'val', secure=True)      # HTTPS only

# Get Cookie
username = request.cookies.get('username')         # Read cookie

# Delete Cookie
resp.set_cookie('username', '', expires=0)         # Delete cookie
resp.delete_cookie('username')                     # Alternative

┌─────────────────────────────────────────────────────────────────────────────┐
│ REQUEST HOOKS (Lifecycle)                                                  │
└─────────────────────────────────────────────────────────────────────────────┘

@app.before_first_request                          # Before first request only
def initialize():
    # Setup database, load config, etc.
    pass

@app.before_request                                # Before every request
def check_login():
    # Check authentication, log request, etc.
    pass

@app.after_request                                 # After every request
def add_header(response):
    # Modify response, add headers, etc.
    return response

@app.teardown_request                              # After request (even if error)
def cleanup(error):
    # Close database, cleanup resources
    pass

@app.teardown_appcontext                           # When app context ends
def shutdown_session(exception=None):
    # Cleanup app-level resources
    pass

┌─────────────────────────────────────────────────────────────────────────────┐
│ LOGGING                                                                     │
└─────────────────────────────────────────────────────────────────────────────┘

app.logger.debug('Debug message')                  # Debug level
app.logger.info('Info message')                    # Info level
app.logger.warning('Warning message')              # Warning level
app.logger.error('Error message')                  # Error level
app.logger.critical('Critical message')            # Critical level

┌─────────────────────────────────────────────────────────────────────────────┐
│ CONFIGURATION                                                               │
└─────────────────────────────────────────────────────────────────────────────┘

# Configuration Methods
app.config['DEBUG'] = True                         # Direct assignment
app.config.from_object('config.DevelopmentConfig') # From object
app.config.from_pyfile('config.py')                # From file
app.config.from_envvar('APP_CONFIG_FILE')          # From environment

# Common Configuration Keys
app.config['SECRET_KEY'] = 'secret'                # Secret key
app.config['DEBUG'] = True                         # Debug mode
app.config['TESTING'] = True                       # Testing mode
app.config['JSON_SORT_KEYS'] = False               # Don't sort JSON keys
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload

┌─────────────────────────────────────────────────────────────────────────────┐
│ COMMON HTTP STATUS CODES                                                   │
└─────────────────────────────────────────────────────────────────────────────┘

200 - OK                                           # Successful request
201 - Created                                      # Resource created
204 - No Content                                   # Success, no content
301 - Moved Permanently                            # Permanent redirect
302 - Found                                        # Temporary redirect
304 - Not Modified                                 # Cached version valid
400 - Bad Request                                  # Invalid request
401 - Unauthorized                                 # Authentication required
403 - Forbidden                                    # Access denied
404 - Not Found                                    # Resource not found
405 - Method Not Allowed                           # Wrong HTTP method
500 - Internal Server Error                        # Server error
503 - Service Unavailable                          # Server down

┌─────────────────────────────────────────────────────────────────────────────┐
│ COMMON PATTERNS & EXAMPLES                                                 │
└─────────────────────────────────────────────────────────────────────────────┘

# Form with Validation
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        if not username:
            flash('Username required', 'error')
            return redirect(url_for('register'))
        # Process registration...
        flash('Registration successful!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')

# API Endpoint
@app.route('/api/users/<int:user_id>')
def get_user(user_id):
    user = {'id': user_id, 'name': 'John'}
    return jsonify(user), 200

# File Upload
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400
    file = request.files['file']
    if file.filename == '':
        return 'Empty filename', 400
    file.save(f'uploads/{file.filename}')
    return 'File uploaded', 201

# Protected Route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please login first', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

# Pagination
@app.route('/posts')
def posts():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    # Get paginated data...
    return render_template('posts.html', posts=posts, page=page)

===============================================================================
"""