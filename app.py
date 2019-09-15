from flask import *
import google.cloud
from create_user import create_user_firebase
from login_scripts.facebook_scrape import fb_login_scrape, fb_add_friend

app = Flask(__name__)

@app.route('/')
def student():
    return render_template('create_user.html')

@app.route('/userhome',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':

      result = request.form
      global fyouze_user
      fyouze_user = result['username']
      
      create_user_firebase(result['username'])
      return render_template(
          'userhome.html',
          username=result['username']
        )

@app.route('/fblogin')
def fb_login():
    return render_template('fb_login.html')

@app.route('/test', methods=['POST', 'GET'])
def login_more():
    if request.method == 'POST':
        result = request.form
        print(result)
        global fb_session
        fb_session = fb_login_scrape(fyouze_user, result['fb_username'], result['fb_password'])
        return render_template(
            'social-media-ui-master/contacts.html'
        )

@app.route('/dashboard')
def dashboard():
    return render_template(
        'social-media-ui-master/contacts.html'
    )

@app.route('/addcontact', methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        result = request.form
        print(result)
        fb_add_friend(fb_session, result['friend_username'], fyouze_user)
    return render_template(
        'social-media-ui-master/contacts.html'
    )

if __name__ == '__main__':
   app.run(debug=True)


