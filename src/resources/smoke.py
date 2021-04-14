"""Module resource Smoke."""
from flask_restful import Resource


class Smoke(Resource):
    """Test class Smoke."""

    def get(self):
        """Test GET request for Smoke class."""
        return {'message': 'Ok'}, 200
