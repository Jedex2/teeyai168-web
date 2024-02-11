from flask import Flask,render_template


app = Flask(__name__)



@app.route('/')
def slot():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('loginForm.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/signin')
def signin():
    return render_template('signinForm.html')

if __name__ == '__main__':
    app.run(debug=True)

