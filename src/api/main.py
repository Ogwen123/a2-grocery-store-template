from flask import Flask, Response, Blueprint
from utils.response import success
from api.test.main import test_bp
import json

# here we create a new "blueprint"
api_bp = Blueprint("api", __name__, url_prefix="/api")
# a blueprint is a way to group routes together
# the first argument, "api" is the name of the blueprint
# the second argument, __name__ will always be __name__
# the third argument, url_prefix is the prefix for all routes in this blueprint
#  so all routes in this blueprint will start with /api, so when we define the route for /, it will be /api/


# here, we are nesting blueprints
api_bp.register_blueprint(test_bp)
# like with classes in object oriented programming, this new blueprint will inherit all the settings from the api_bp blueprint
# so the route for / will be /api/test/ (the extra /test is defined in the test_bp blueprint in /src/api/test/main.py)

# here we define a route for the root of the blueprint
@api_bp.route("/") # this route is actually /api/
def root():
    return success("Hello, world!")