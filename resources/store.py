from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help='This field cannot be left blank!')

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': f'Store {name} not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f'An item with name {name} already exists'}, 400
        store = StoreModel(name)
        store.save_to_db()
        return store.json(), 201

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {'message': 'Store deleted'}
        return {'message': 'Store not found'}, 404


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
