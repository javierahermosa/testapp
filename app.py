import os
from flask import Flask, render_template, send_from_directory, request, flash

# initialization
app = Flask(__name__)
app.config.update(
    DEBUG = True
)
app.secret_key = "talca"

# controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
	return render_template('index.html')

@app.route('/',methods=['GET','POST'])
def post():
	result = request.form['expression']
	flash(result)
	return index()

# launch
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run()
