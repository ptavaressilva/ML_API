from api import app
from flask import json

# Literals
TITANIC = '/titanic'
CONTENT_TYPE = 'application/json'
MSG_MISS = 'Missing required parameter in the JSON body'


def test_prediction():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10",
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert "That passenger probably" in data['Prediction']


def test_missing_age():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert MSG_MISS in data['message']['Age']


def test_missing_fare():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert MSG_MISS in data['message']['Fare']


def test_missing_sibsp():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "Fare": "123.0",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert MSG_MISS in data['message']['SibSp']


def test_missing_sex():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "Fare": "123.0",
            "SibSp": "2",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert MSG_MISS in data['message']['Sex']


def test_missing_cabin():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "male",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert MSG_MISS in data['message']['Cabin']


def test_missing_embarked():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "A"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert MSG_MISS in data['message']['Embarked']


def test_age_is_num():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "abc",
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert 'is not a valid number of years' in data['message']


def test_fare_is_num():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "Fare": "abc",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert 'is not a valid Fare in british pounds' in data['message']


def test_sibsp_is_num():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "Fare": "123.0",
            "SibSp": "abc",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert 'is not a valid SibSp value' in data['message']


def test_sex_is_valid():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10.0",
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "abc",
            "Cabin": "A",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert 'is not a valid Sex value' in data['message']


def test_cabin_is_valid():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10",
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "abc",
            "Embarked": "S"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert 'is not a valid Cabin letter' in data['message']


def test_embarked_is_valid():
    response = app.test_client().get(
        TITANIC,
        data=json.dumps({
            "Age": "10",
            "Fare": "123.0",
            "SibSp": "2",
            "Sex": "male",
            "Cabin": "A",
            "Embarked": "abc"
        }),
        content_type=CONTENT_TYPE,
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 400
    assert 'is not a valid port of departure letter' in data['message']
