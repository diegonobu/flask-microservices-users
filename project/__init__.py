import os
from flask import jsonify
from flask.app import Flask

app = Flask(__name__)

app.settings = os.getenv('APP_SETTINGS')
app.config.from_object('project.config.DevelopmentConfig')


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong!'
    })