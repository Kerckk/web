from flask import Flask, render_template, request
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/css/styles.css')
def styles():
    return app.send_static_file('css/styles.css'),  {'Content-Type': 'text/css'}

@app.route('/greet', methods=["POST"])
def greet():
    name = request.form['name']
    return render_template('greet.html', name=name)
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


