from api.ekyc_card import *
from flask import Flask, request
import sys
import os


app = Flask(__name__)
api = Api(app)
port = 5100

if sys.argv.__len__() > 1:
    port = sys.argv[1]
print("Api running on port : {} ".format(port))

class topic_tags(Resource):
    def get(self):
        return {'hello': 'world world'}


api.add_resource(topic_tags, '/')
api.add_resource(ping, '/ping')
api.add_resource(ekyc, '/getocr')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)