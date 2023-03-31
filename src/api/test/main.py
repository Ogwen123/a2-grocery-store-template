# this file is a test route to demonstrate how to create a new blueprint and folder structure
# you can delete it if you dont need it
from flask import Flask, Response, Blueprint
from utils.response import success
import json

test_bp = Blueprint("test", __name__, url_prefix="/test")

@test_bp.route("/") # this route is actually /api/test/
def test(): # the name of the function can be anything, just make sure it is unique and descriptive
    return success("test!") # change this text to see it change on the /test page!