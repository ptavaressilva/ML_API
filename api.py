from flask import Flask
from flask_restful import Resource, Api, reqparse
# import pandas as pd
# from sklearn.preprocessing import OneHotEncoder, StandardScaler

# import pickle

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('Age', required=True)
parser.add_argument('Fare', required=True)
parser.add_argument('SibSp', required=True)
parser.add_argument('Sex', required=True)
parser.add_argument('Cabin', required=True)
parser.add_argument('Embarked', required=True)


class Titanic(Resource):
    def get(self):  # , SibSp, Fare, Sex, Cabin, Embarked
        args = parser.parse_args()

        # 'Age' must be float
        try:
            age = float(args['Age'])
        except:
            return {
                'message': f"'{args['Age']}' is not a valid number of years (must be float or int)."
            }, 200

        # 'SibSp' must be int
        try:
            SibSp = int(args['SibSp'])
        except:
            return {
                'message': "'{}' is not a valid SibSp value (number of siblings and spouses aboard the Titanic must be integer).".format(args['SibSp'])
            }, 200

        # 'Fare' must be float
        try:
            Fare = float(args['Fare'])
        except:
            return {
                'message': "'{}' is not a valid Fare in british pounds value (must be float or int).".format(args['Fare'])
            }, 400

        # 'Sex' is in ['female', 'male']
        if args['Sex'] not in ['female', 'male']:
            return {
                'message': f"'{args['Sex']}' is not a valid Sex value (must be 'female' or 'male')."
            }, 400

        # 'Cabin' is in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'W', 'Z']
        if args['Cabin'] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'W', 'Z']:
            return {
                'message': f"'{args['Cabin']}' is not a valid Cabin letter (must be 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'W' or 'Z')."
            }, 400

        # 'Embarked' is in ['C', 'Q', 'S']
        if args['Embarked'] not in ['C', 'Q', 'S']:
            return {
                'message': f"'{args['Embarked']}' is not a valid port of departure letter (must be 'C', 'Q' or 'S')."
            }, 400

    #   normalize 'Age', 'SibSp', 'Fare'
    #         scaler = json.loads(scaler_json)

    #   encode 'Sex', 'Cabin', 'Embarked'
    #         encoder = json.loads(encoder_json)

        # return data and 200 OK
        return {'survived': 'I will tell you soon'}, 200


api.add_resource(Titanic, '/titanic')  # add endpoint

if __name__ == '__main__':
    # run our Flask app in development
    app.run(host='0.0.0.0', port=6000, debug=True)
