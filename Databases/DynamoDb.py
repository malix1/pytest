import boto3


class Db:
    client = ""

    def __init__(self):
        self.client = boto3.client("dynamodb", region_name="us-east-2")

    def save_book(self, book):
        response = self.client.put_item(TableName="table1", Item={
            "BookID": {
                "S": "123"
            },
            "name": {
                "S": book["name"]
            },
            "type": {
                "S": book["type"]
            }
        })
        return response

    def remove_book(self, book):
        response = self.client.delete_item(TableName="table1", Key={
            "BookID": {
                "S": book["BookID"]
            },
            "name": {
                "S": book["name"]
            },
            "type": {
                "S": book["name"]
            }
        })
        return response

    def get_book(self, book):
        response = self.client.get_item(TableName="table1", Key={
            "BookID": {
                "S": book["BookID"]
            },
            "name": {
                "S": book["name"]
            },
            "type": {
                "S": book["name"]
            }
        })
        return response
