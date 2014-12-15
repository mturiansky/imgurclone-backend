from flask import Flask
import os

username = ''
app.config['SUPER_SECRET_KEY'] = '' #should be the same as the frontend

app = Flask(__name__)
app.secret_key = 'this is a secret key'
app.config['UPLOADS_FOLDER'] = os.path.join(os.getcwd(),"uploads")
app.config['FRONTEND_URL'] = 'http://%s.pythonanywhere.com' % username
