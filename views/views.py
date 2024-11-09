from flask import Blueprint, redirect, url_for, request, render_template
from services.services import *

views_bp = Blueprint('views', __name__)

@views_bp.route('/')
def hello_world():
    return redirect(url_for('views.login'))

@views_bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        #email = request.form['email']
        #senha = request.form['senha']
        return redirect('/dashboard')
    else:
        return render_template('login.html')
    
@views_bp.route('/recover', methods=['POST', 'GET'])
def recover():
    return render_template('recover.html')

@views_bp.route('/register', methods=['POST', 'GET'])
def register():
    return render_template('register.html')

@views_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', active_page='dashboard')

@views_bp.route('/corridas')
def corridas():
    return render_template('corridas.html', active_page='corridas')

@views_bp.route('/prever-corridas')
def prever_corridas():
    return render_template('prever-corridas.html', active_page='prever_corridas')