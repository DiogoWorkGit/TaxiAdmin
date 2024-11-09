from datetime import timedelta
import json

class Config:
    def js_read(filename: str):
        with open(filename) as j_file:
            return json.load(j_file)
    data = js_read('env_variables.json')
    
    SECRET_KEY=data['secret_key_flask']
    
    SQLALCHEMY_DATABASE_URI = \
        '{SGBD}://{usuario}:{senha}@{servidor}:{porta}/{database}'.format(
            SGBD        = 'mysql+mysqlconnector',
            usuario     = data['config_flask_info']['db_usuario'],
            senha       = data['config_flask_info']['db_password'],
            servidor    = data['config_flask_info']['db_hostname'],
            porta       = data['config_flask_info']['db_port'],
            database    = data['config_flask_info']['db_name']
        )
        
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=50)