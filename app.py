from flask import *
import google.cloud
from create_user import create_user_firebase
from login_scripts.facebook_scrape import fb_login_scrape, fb_add_friend
from login_scripts.linkedin_scrape import linkedin_login_scrape, linkedin_add_friend
from login_scripts.instagram_scrape import ig_login_scrape, ig_add_friend

import firebase
from firebase import firebase

app = Flask(__name__)
db = firebase.FirebaseApplication("https://social-media-app-e8fe0.firebaseio.com/")

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

@app.route('/linkedinlogin')
def linkedin_login():
    return render_template('linkedin_login.html')

@app.route('/iglogin')
def ig_login():
    return render_template('ig_login.html')

@app.route('/fbprocessing', methods=['POST', 'GET'])
def fb_processing():
    if request.method == 'POST':
        result = request.form
        print(result)
        global fb_session
        fb_session = fb_login_scrape(fyouze_user, result['fb_username'], result['fb_password'])

        return render_template(
            'userhome.html',
            socialmedia = db.get('/users', None)[fyouze_user]
        )

@app.route('/linkedinprocessing', methods=['POST', 'GET'])
def linkedin_processing():
    if request.method == 'POST':
        result = request.form
        print(result)
        global linkedin_session
        linkedin_session = linkedin_login_scrape(fyouze_user, result['linkedin_username'], result['linkedin_password'])

        return render_template(
            'userhome.html',
            socialmedia = db.get('/users', None)[fyouze_user]
        )

@app.route('/igprocessing', methods=['POST', 'GET'])
def ig_processing():
    if request.method == 'POST':
        result = request.form
        print(result)
        global ig_session
        ig_session = ig_login_scrape(fyouze_user, result['ig_username'], result['ig_password'])

        return render_template(
            'userhome.html',
            socialmedia = db.get('/users', None)[fyouze_user]
        )

@app.route('/dashboard')
def dashboard():
    return render_template(
        'social-media-ui-master/contacts.html',
        socialmedia = db.get('/users', None)[fyouze_user]
    )

@app.route('/addcontact', methods=['POST', 'GET'])
def add_contact():
    if request.method == 'POST':
        result = request.form
        print(result)
        if 'fb' in result:
            fb_add_friend(fb_session, result['friend_username'], fyouze_user)
        if 'linkedin' in result:
            linkedin_add_friend(linkedin_session, result['friend_username'], fyouze_user)
        if 'ig' in result:
            ig_add_friend(ig_session, result['friend_username'], fyouze_user)

    return render_template(
        'social-media-ui-master/contacts.html'
    )

if __name__ == '__main__':
   app.run(debug=True)


