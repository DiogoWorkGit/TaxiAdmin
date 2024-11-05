from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('login'))

@app.route('/dashboard/<email>/<senha>')
def dashboard(email, senha):
    if not email or not senha:
        return redirect(url_for('login'))
    else:
        return 'Welcome %s' % email

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        return redirect(url_for('dashboard', email=email, senha=senha))
    else:
        return render_template('login.html')
    
@app.route('/recover', methods=['POST', 'GET'])
def recover():
    return render_template('recover.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

if __name__ == '__main__':

    app.run(debug=True)