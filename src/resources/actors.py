"""Module resource for actors."""
from flask_restful import Resource

from src.schemas.actors import ActorSchema


class ActorListApi(Resource):
    actor_schema = ActorSchema()
    
    def get(self, uuid=None):
        if not uuid:
            pass
        pass

    def post(self):
        pass
        
    def put(self):
        pass

    def patch(self):
        pass
    
    def delete(self):
        pass