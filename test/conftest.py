import pytest
import os
import boto3
from moto import mock_dynamodb2
from Databases.StudentDB import StudentDB
from Databases.DynamoDb import Db


@pytest.fixture(scope="session")
def db():
    print("\nconnecting db")
    db = StudentDB()
    db.connect("mock_datas/data.json")
    yield db
    db.close()


@pytest.fixture(scope='module')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture(scope="module")
def dynamoDb(aws_credentials):
    print("connection dynamo db")
    with mock_dynamodb2():
        database = Db()
        database.client.create_table(TableName="table1",
                                     KeySchema=[
                                         {"AttributeName": "BookID",
                                          "KeyType": "HASH"},
                                         {"AttributeName": "name", "KeyType": ""},
                                         {"AttributeName": "type", "KeyType": ""}

                                     ],
                                     AttributeDefinitions=[
                                         {"AttributeName": "name",
                                          "AttributeType": "S"},
                                         {"AttributeName": "type",
                                          "AttributeType": "S"},
                                         {"AttributeName": "BookID",
                                          "AttributeType": "S"}
                                     ]
                                     )
        waiter = database.client.get_waiter("table_exists")
        waiter.wait(TableName="table1")
        yield database
