from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import pickle
import json

scaler = pickle.load(open("ML/scaler.pkl", "rb"))
encoder = pickle.load(open("ML/encoder.pkl", "rb"))
model = pickle.load(open("ML/DecisionTreeClassifier.pkl", "rb"))

with open('./Titanic_ML_regressor-1-resolved.json') as openapi_file:  # Swagger file
    openapi_description = json.load(openapi_file)

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

    def options(self):
        print(openapi_description)
        return {'OpenAPI document': openapi_description}

    def get(self):  # , SibSp, Fare, Sex, Cabin, Embarked
        args = parser.parse_args()

        # 'Age' must be float
        try:
            age = float(args['Age'])
        except:
            return {
                'message': f"'{args['Age']}' is not a valid number of years (must be float or int)."
            }, 400

        # 'SibSp' must be int
        try:
            sibsp = int(args['SibSp'])
        except:
            return {
                'message': "'{}' is not a valid SibSp value (number of siblings and spouses aboard the Titanic must be integer).".format(args['SibSp'])
            }, 400

        # 'Fare' must be float
        try:
            fare = float(args['Fare'])
        except:
            return {
                'message': "'{}' is not a valid Fare in british pounds value (must be float or int).".format(args['Fare'])
            }, 400

        # 'Sex' is in ['female', 'male']
        if args['Sex'] not in ['female', 'male']:
            return {
                'message': f"'{args['Sex']}' is not a valid Sex value (must be 'female' or 'male')."
            }, 400

        sex = args['Sex']

        # 'Cabin' is in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'W', 'Z']
        if args['Cabin'] not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'W', 'Z']:
            return {
                'message': f"'{args['Cabin']}' is not a valid Cabin letter (must be 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'T', 'W' or 'Z')."
            }, 400

        cabin = args['Cabin']

        # 'Embarked' is in ['C', 'Q', 'S']
        if args['Embarked'] not in ['C', 'Q', 'S']:
            return {
                'message': f"'{args['Embarked']}' is not a valid port of departure letter (must be 'C', 'Q' or 'S')."
            }, 400

        embarked = args['Embarked']

        df1 = pd.DataFrame(index=[1], data={'Age': age,
                                            'Fare': fare,
                                            'SibSp': sibsp,
                                            'Sex': sex,
                                            'Cabin': cabin,
                                            'Embarked': embarked})
        df1.loc[:, ['Age', 'Fare', 'SibSp']] = scaler.transform(
            df1.loc[:, ['Age', 'Fare', 'SibSp']])
        df1_encoded = pd.DataFrame(encoder.transform(
            df1[['Sex', 'Cabin', 'Embarked']]))
        df1_encoded.index = [1]
        df1 = df1.drop(columns=['Sex', 'Cabin', 'Embarked'])
        df1 = pd.concat([df1, df1_encoded], axis=1)

        if model.predict(df1.values)[0] == 0:
            return {'Prediction': 'That passenger probably did not survive'}, 200
        else:
            return {'Prediction': 'That passenger probably survived!'}, 200


api.add_resource(Titanic, '/titanic')  # add endpoint

if __name__ == '__main__':
    # run our Flask app in development
    app.run(host='0.0.0.0', port=6000, debug=True)
