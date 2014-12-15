from flask import redirect, send_from_directory, request
from setup import app
import os

@app.route('/', methods=['GET','POST'])
def home():
	if request.method == 'POST':
		if 'secret_key' in request.form and request.form['secret_key'] == app.config['SUPER_SECRET_KEY']:
			if 'name' in request.form and 'img' in request.files:
				f = request.files['img']
				f.save(os.path.join(app.config['UPLOADS_FOLDER'],request.form['name']+'.jpg'))
	return redirect(app.config['FRONTEND_URL'])

@app.route('/delete', methods=['POST'])
def delete():
	if 'secret_key' in request.form and request.form['secret_key'] == app.config['SUPER_SECRET_KEY']:
		if 'name' in request.form:
			os.remove(os.path.join(app.config['UPLOADS_FOLDER'],request.form['name']+'.jpg'))

@app.route('/img/<img_id>')
def view_image(img_id):
	return send_from_directory(app.config['UPLOADS_FOLDER'], img_id+'.jpg')