import os
from model import power
from flask import Flask, request

app = Flask(__name__)

HOST_NAME = os.environ.get('OPENSHIFT_APP_DNS', 'localhost')
APP_NAME = os.environ.get('OPENSHIFT_APP_NAME', 'flask')
IP = os.environ.get('OPENSHIFT_PYTHON_IP', '127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT', 8080))
HOME_DIR = os.environ.get('OPENSHIFT_HOMEDIR', os.getcwd())


@app.route('/', methods=['GET'])
def model():
    """http://127.0.0.1:8080/?number=16"""
    number = request.args.get('number', default=100000000000000000000000000000000000000000000000000000000000000000000000000000001, type=int)
    return 'กำลังสองของ {} คือ {} จ้า'.format(number, power(number))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
