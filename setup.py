from flask import Flask
import os

app = Flask(__name__)

username = ''
app.config['SUPER_SECRET_KEY'] = 'blah' #should be the same as the frontend

app.secret_key = 'this is a secret key'
app.config['UPLOADS_FOLDER'] = os.path.join(os.getcwd(),"uploads")
#app.config['FRONTEND_URL'] = 'http://%s.pythonanywhere.com' % username
app.config['FRONTEND_URL'] = 'http://127.0.0.1:5000/'