from flask import *
from create_user import create_user_firebase

app = Flask(__name__)

@app.route('/')
def home():
    return 'home page'

@app.route('/create', methods=["GET","POST"])
def create_user():
    return render_template("create_user.html")

@app.route('/userhome', methods=["GET"])
def userhome():
    user = request.form.get("username")
    psw = request.form.get("password")
    create_user_firebase(user,psw)
    return 'Welcome {}!'.format(user)


