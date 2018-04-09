from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True  

@app.route("/infoform")
def user_signup_form():
    return render_template("infoform.html")

@app.route("/infoform" methods=['POST'])
def valadate_info():

    username=request.form['username']
    password=request.form['password']
    verify_password=request.form['verify_password']
    email=request.form['email']

    username_error=""
    password_error=""
    verify_password_error=""
    email_error=""

    if username <3 or username >20:
        username_error="The username must be between 3-20 characters."
    elif username==0:
        username_error="You must provide a username."
    elif username.isalph()==False:
        username_error="The username can contain only letters with no spaces."


    return render_template('addinfo.html', username=username, password=password, verify_password=verify_password,
    email=email, username_error=username_error, password_error=password_error,
    verify_password_error=verify_password_error, email_error=email_error)

@app.route("/welcome",)
def welcome():
    name=request.args.get('name')
    return render_template("welcome.html", username=username())



@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('infoform.html', error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()