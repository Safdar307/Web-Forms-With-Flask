from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/submit', methods=['POST'])
def submit():
    feedback_data = {
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "message": request.form.get('message')
    }

   
    if not all(feedback_data.values()):
        return render_template('result.html', message="❌ Error: All fields are required.", data=None)

   
    return render_template('result.html', data=feedback_data)

if __name__ == '__main__':
    app.run(debug=True)
