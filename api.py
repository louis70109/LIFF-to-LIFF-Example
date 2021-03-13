from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv


load_dotenv()

from controller.liff_controller import LiffAController, LiffBController

app = Flask(__name__)
CORS(app)

api = Api(app)
api.add_resource(LiffAController, '/liff/a')
api.add_resource(LiffBController, '/liff/b')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
