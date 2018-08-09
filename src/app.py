from flask import Flask, request
from flask_restful import Resource, Api

# define the app
app = Flask(__name__)
api = Api(app)

# items list, that will contain a dictionary
items = []

# define the resource
class Item(Resource):
    def get(self, name):
        # Can do it like this with for loop
        # for item in items:
        #     if item['name'] == name:
        #         return item

        # or can use lambda filter function
        item = next(filter(lambda x: x['name'] == name, items))
        return {'item': item}, 200 if item else 404
    
    def post(self, name):
        data = request.get_json()
        # if you not sure if client will send you json you can force equals true
        # data = request.get_json(silent=True)
        # data = request.get_json(force=True)
        item = {'name': name, 'price': data['price'] }
        items.append(item)
        return item, 201

class ItemList(Resource):
    def get(self):
        return { 'items': items }

api.add_resource(Item, '/student/<string:name>')
api.add_resource(ItemList, '/items')

app.run(port=5080, debug=True)
