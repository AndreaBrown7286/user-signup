from flask import Flask, request, redirect, render_template
import cgi, string

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

    if len(username) <3 or len(username) >20 or username=='' or str.isalpha(username)==False:
        username_error="The username must be between 3-20 characters with no spaces."
        username=username

    if len(password) <3 or len(password) >20 or password=='' or str.isalpha(password)==False:
        password_error="The password must be between 3-20 characters with no spaces."
        password=''

    if password != verify_password:
        verify_password_error="Your passwords do not match."
        verify_password=''

    if email == "":
        email= ""
    else:
        if not email == "": 
            if len(email)<3 or len(email) >20 or email==" " or ('@' and '.' not in email):
                email_error="That is not a valid email." 
                email=email
    
        

    if not username_error and not password_error and not verify_password_error and not email_error:
        return render_template("welcome.html", username=username)
    else:
        return render_template('infoform.html', username=username, password=password, 
            verify_password=verify_password, email=email, username_error=username_error, 
            password_error=password_error, verify_password_error=verify_password_error, 
            email_error=email_error)

app.run()