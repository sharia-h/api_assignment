from http import HTTPStatus
from flask import Flask, Response, json
class APIResponse:
    def __init__(self, message, data=None, status=HTTPStatus.OK, meta=None):
        self.payload = {
            "status": True,
            "data": data if data else {},
            "message": message,
            "type": "success",
            "httpStatusCode": status,
        }
        self.status = status
 
    def to_json(self):
        return Response(
            json.dumps(self.payload), status=self.status, mimetype="application/json"
        )

 
class APIError(Exception):
    def __init__(self, message, data=None, status=HTTPStatus.INTERNAL_SERVER_ERROR):
        self.payload = {
            "status": False,
            "data": data if data else {},
            "message": message,
            "type": "fail",
            "httpStatusCode": status,
        }
        self.status = status
 
    def to_json(self):
        return Response(
            json.dumps(self.payload), status=self.status, mimetype="application/json"
        )