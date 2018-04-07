from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True  

def user_signup():
    return render_template("addinfo.html")

@app.route("/welcome" method = ["POST"])
def welcome():
    return render_template("welcome.html", username=username())


@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('addinfo.html', watchlist=(), 
        error=encoded_error and cgi.escape(encoded_error, quote=True))

app.run()