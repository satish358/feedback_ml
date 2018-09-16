from flask import Flask, render_template, session, request, url_for, redirect
from functools import wraps
import loginHelper
import getData

app = Flask(__name__)
app.secret_key = "helloFriendChaiPeeLo"

def isLogIn(f):
    @wraps(f)
    def wrap(*args,**kwargs):
        if 'loggedIn' in session:
            return f(*args,**kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@app.route("/",methods=['POST','GET'])
def login():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        email = request.form['email']
        passwd = request.form['password']
        login_status = loginHelper.checkUserValidorNot(email,passwd)
        if login_status['status_code'] == 200:
            session['loggedIn'] = True
            session['token'] = login_status['token']
            return redirect(url_for('homepage'))
        else:
            return redirect(url_for('login'))


@app.route("/homepage")
@isLogIn
def homepage():
    data = getData.getFeedData(session['token'])
    data_len = len(data)
    return render_template('homepage.html',feeds=data,data_len=data_len)

@app.route("/feeds/<int:app_id>")
@isLogIn
def getAppIdFeeds(app_id):
    tempData = getData.getFeedData(session['token'])
    data = getData.sortFeedsByAppID(tempData,app_id)
    data_len = len(data)
    return render_template('homepage.html', feeds=data, data_len=data_len)


@app.route('/logout')
def logout():
   session.pop('loggedIn', None)
   session.pop('token',None)
   return redirect(url_for('login'))
 
if __name__ == "__main__":
    app.run(debug=True, host='172.16.4.241')
