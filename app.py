from flask import *
import firebase_admin
import google.cloud
from firebase_admin import credentials, firestore
from create_user import create_user_firebase

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('create_user.html')

@app.route('/userhome',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      create_user_firebase(result['username'], result['password'])
      return render_template(
          'userhome.html',
          username=result['username']
        )

if __name__ == '__main__':
   app.run(debug=True)


