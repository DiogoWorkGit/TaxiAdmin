from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return redirect(url_for('login'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #email = request.form['email']
        #senha = request.form['senha']
        return redirect('/dashboard')
    else:
        return render_template('login.html')
    
@app.route('/recover', methods=['POST', 'GET'])
def recover():
    return render_template('recover.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')

@app.route('/corridas')
def corridas():
    return render_template('corridas.html', active_page='corridas')

@app.route('/prever-corridas')
def prever_corridas():
    return render_template('prever-corridas.html', active_page='prever_corridas')

if __name__ == '__main__':

    app.run(debug=True)