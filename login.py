import pyrebase
from flask import request


class Login(object):

    def __init__(self):
        
        self.config = {
        "apiKey": "AIzaSyDjjtDzIgOQDYZiFaG8BcoM3AI44tCYrCk",
        "authDomain": "acehack-3eddb.firebaseapp.com",
        "databaseURL": "https://acehack-3eddb-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "acehack-3eddb",
        "storageBucket": "acehack-3eddb.appspot.com",
        "messagingSenderId": "650696029031",
        "appId": "1:650696029031:web:398aa743782722b516b5c2",
        "measurementId": "G-XKMDTLYK90"
        };


        self.firebase = pyrebase.initialize_app(self.config)

        self.auth = self.firebase.auth()

    def kisan_login(self):

        if request.method == 'POST':
            kisan_id = request.form['kisan_id']
            password = request.form['password']
            email = 'kisan'+kisan_id+'@gmail.com'
            try:
                user = self.auth.sign_in_with_email_and_password(email, password)
                # user['id']
                return 'successful',email
            except:
                return 'unsuccessful'