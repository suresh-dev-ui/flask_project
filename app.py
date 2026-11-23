from flask import Flask ,request,render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/login',methods = ['POST'])
def login():
    username = request.form['username']
    email = request.form['email']
    branch = request.form['branch']
    return f"""
<h2>Registartion successsfull</h2>
Name:{username}<br>
Email:{email}<br>
Branch:{branch}
"""

if __name__ == "__main__":
    app.run(debug=True)