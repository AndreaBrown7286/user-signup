from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True  

@app.route("/")
def index():
    return render_template('infoform.html')

@app.route("/", methods=['POST'])
def validate():   

    username=request.form['username']
    password=request.form['password']
    verify_password=request.form['verify_password']
    email=request.form['email']

    username_error=""
    password_error=""
    verify_password_error=""
    email_error=""

    if len(username) <3 or len(username) >20 or username=='' or username==' ':
        username_error="The username must be between 3-20 characters with no spaces."
        username=username

    if len(password) <3 or len(password) >20 or password=='' or password==' ':
        password_error="The password must be between 3-20 characters with no spaces."
        password=''

    if password != verify_password:
        verify_password_error="Your passwords do not match."
        password=''

    if email =="":
        email=email
    if len(email) <3 or len(email) >20 or email==' ':
        email_error="The email must be between 3-20 characters with no spaces."
    if '@' or '.' not in email:
        email_error="That is not a valid email." 
        email=email

    if not username_error or not password_error or not verify_password_error or not email_error:
        return redirect('/welcome')
    else:
        return render_template('infoform.html', username=username, password=password, 
            verify_password=verify_password, email=email, username_error=username_error, 
            password_error=password_error, verify_password_error=verify_password_error, 
            email_error=email_error)

@app.route("/welcome", methods=['POST','GET'])
def welcome():
    username=request.form['username']
    return render_template("welcome.html", username=username)

app.run()