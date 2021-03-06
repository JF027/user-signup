from flask import Flask, request, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/register", methods=['GET'])
def register_page():
    return render_template("signup.html")

@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email = cgi.escape(request.form['email'])

    username_error = ""
    password_error = ""
    password2_error = ""
    email_error = ""
#Your username should contain no spaces and consist of more than 3 characters and less than 20 characters.
    if not username:
        username_error = "Please enter a username."
    if not password:
        password_error = "Please enter a password."
    elif len(password) < 3:
        password_error = "Password should be between 3 and 20 characters."
    elif len(password) > 20:
        password_error = "Password should be between 3 and 20 characters."
   # else:
       # contains_number = False
       # for char in password:
          #  if char.isdigit():
          #      contains_number = True
        #if not contains_number:
         #   password_error = "Enter a number in the password."
    if password2 != password:
        password2_error = "Please match this password with the first one."


    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match == None:
        email_error = "Please enter a valid email."
   # elif len(email) < 3:
    #    email_error = "Your email should contain no spaces and consist of more than 3 characters and less than 20 characters."

    if username_error or password_error or password2_error or email_error:
        return render_template("signup.html", username=username, usernameError=username_error, password=password, passwordError=password_error, password2=password2, password2Error=password2_error, email=email, emailError=email_error)

    return 'Welcome, ' + username 

@app.route("/")
def index():
    return render_template('signup.html')

app.run()