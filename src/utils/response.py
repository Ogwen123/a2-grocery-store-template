# this is a pre-built standard response format
# you do not need to use it, but it is here for your convenience

import json
from flask import Response
from http import HTTPStatus

# use this function to return an error
def error(message, status_code=400):
    j = json.dumps(
        {
            "success": False,
            "code": status_code,
            # get the status code message from the status code
            "message": str(HTTPStatus(status_code).phrase),
            "error": message,
        }, allow_nan=False
    )
    
    return Response(j, status=status_code, mimetype="application/json")

# use this function when everything is ok and you want to return data
def success(data, status_code=200):
    j = json.dumps(
        {
            "success": True,
            "code": status_code,
            # get the status code message from the status code
            "message": str(HTTPStatus(status_code).phrase),
            "data": data,
        }, allow_nan=False
    )
    
    return Response(j, status=status_code, mimetype="application/json", headers={"access-control-allow-origin": "*"})