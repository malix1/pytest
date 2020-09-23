import pytest
import boto3
from moto import mock_dynamodb2
from Databases.DynamoDb import Db


def test_save_book(dynamoDb):
    book = {"name": "lotr", "type": "type"}
    response = dynamoDb.save_book(book)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200


def test_remove_book(dynamoDb):
    book = {"name": "lotr", "type": "type", "BookID": "123"}
    response = dynamoDb.save_book(book)
    response = dynamoDb.remove_book(book)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200


def test_get_book(dynamoDb):
    book = {"name": "lotr", "type": "type", "BookID": "123"}
    response1 = dynamoDb.save_book(book)
    response = dynamoDb.get_book(book)
    assert response['ResponseMetadata']['HTTPStatusCode'] == 200
