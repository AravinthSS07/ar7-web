from flask import *

app = Flask(__name__)

app.secret_key = "ssassk@2004"

@app.route('/')
def home():
	msg = ''
	return render_template("index.html")

@app.route('/projects')
def projects():
	msg = ''
	return render_template("projects.html")

@app.route("/email")
def email():
	msg = ''
	return render_template("email.html")

@app.route("/branding")
def branding():
	msg = 'https://dl.dropboxusercontent.com/s/b212ivunjwholzi/Ar7MediaKit.zip?dl=0'
	return render_template("logos.html", mediadownload_host=msg)

@app.route('/livestream/ar7')
def ar7live():
  return redirect('https://aravinthss07.github.io/twitchplayer/ar7.html')

#@app.route('/diwaliwishes')
#def diwaliwishes():
#  msg = ''
#  return render_template('diwaliwishes.html')

@app.route('/youtube')
def youtube():
	return redirect('https://www.youtube.com/channel/UCA5LP7N2K3A_18qgYQ6jGFw', code=302)

@app.route('/twitch')
def twitch():
	return redirect('https://twitch.tv/ar7twitch', code=302)

@app.route('/github')
def github():
	return redirect('https://github.com/AravinthSS07', code=302)

@app.route('/soundcloud')
def soundcloud():
	return redirect('https://soundcloud.com/official-ar7', code=302)

@app.route('/bandlab')
def bandlab():
  return redirect('https://www.bandlab.com/official_ar7')

@app.errorhandler(401)
def not_perms(e):
  num = '401'
  msg = "Hey I guess you don't have the permission to open this page"
  return render_template('handler.html', tittle=num, msg=msg)

@app.errorhandler(404)
def not_found(e):
  num = '404'
  msg = "Looks like you're lost"
  return render_template('handler.html', tittle=num, msg=msg)

@app.errorhandler(501)
def not_prepared(e):
  num = '501'
  msg = "Oh! we're not yet Prepared"
  return render_template('handler.html', tittle=num, msg=msg)

@app.errorhandler(502)
def bad_way(e):
  num = '502'
  msg = "Bad link maybe try a good link?"
  return render_template('handler.html', tittle=num, msg=msg)

@app.errorhandler(503)
def not_there(e):
  num = '503'
  msg = "Sorry there is nothing like that here"
  return render_template('handler.html', tittle=num, msg=msg)

if __name__ == '__main__':
	app.run(threaded=True, port=5000)