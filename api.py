from flask import Flask
from flask_restful import Resource, Api, reqparse
#import pandas as pd
#from sklearn.preprocessing import OneHotEncoder, StandardScaler

#import pickle

app = Flask(__name__)
api = Api(app)


class Titanic(Resource):
    def get(self):

        # imput features:
        #   'Age'
        #   'SibSp'
        #   'Fare'
        #   'Sex' is in ['female', 'male']
        #   'Cabin' is in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'W', 'Z']
        #   'Embarked' is in ['C', 'Q', 'S']

        # normalize 'Age', 'SibSp', 'Fare'
     #       scaler = json.loads(scaler_json)

        # encode 'Sex', 'Cabin', 'Embarked'
     #       encoder = json.loads(encoder_json)

        # return data and 200 OK
        return {'survived': 'I will tell you soon'}, 200


api.add_resource(Titanic, '/titanic')  # add endpoints

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)  # run our Flask app
