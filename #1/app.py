from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        message = "Error: Both username and password fields are required."
    else:
        message = f"Welcome, {username}!"

    return render_template('result.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
