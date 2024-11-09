from flask import Flask, redirect, url_for, request, render_template
from views.views import views_bp

app = Flask(__name__)
app.config.from_object('config.Config')

app.register_blueprint(views_bp)

if __name__ == '__main__':

    app.run(debug=True)