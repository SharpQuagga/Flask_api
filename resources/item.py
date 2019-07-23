# App.py ka hai ye saara code
# import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import JWT, jwt_required
from models.item import ItemModel

items = []

class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="Can't left blank")
    
    @jwt_required()   # This will make the JWT token necessary to perform the function
    def get(self, name):
        item =ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'Item not found'}, 404    
        # item = next(filter(lambda x:x['name'] == name,items),None)
        # # for item in items:
        # #     if item['name'] == name:
        # #         return item
        # return {'item':item}, 200 if item else 404 # Status code for  Error

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':"An item with name '{}' already exists".format(name)}, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'])
        
        try:
            item.insert()
            # ItemModel.insert(item)
        except:
            return {'message':"Eror occured inserting"}    

        return item.json(), 501 # INTERNAL server error
        

    def delete(self, name):

        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {'message': 'Item Deleted'}    

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query,(name,))

        # connection.commit()
        # connection.close()

        # # global items
        # # items = list(filter(lambda x:x['name'] != name,items))
        # return {'message': 'Item Deleted'}


    def put(self, name):
        data = Item.parser.parse_args()
        # data = request.get_json()
        
        item = ItemModel.find_by_name(name)
        # updated_item = ItemModel(name,data['price']) 
        
        if item is None:
            item = ItemModel(name, data['price'])
            # try:

            #     # updated_item.insert()
            #     # ItemModel.insert(updated_item)
            # except:
            #     return {'message':"ERROR"}    
        else:
            item.price = data['price']
            # try:
            #     updated_item.update()
            #     # ItemModel.update(updated_item)    
            # except:
            #     return {'message':"ERROR"}    
        item.save_to_db()
        return item.json()

        # item = next(filter(lambda x: x['name'] == name,items),None)
        # if item is None:
        #     item = {'name':name,'price':data['price']}
        #     items.append(item)
        # else:
        #     item.update(item)   
        # return item    

    
class ItemList(Resource):
    def get(self):
        {'items': [item.json() for item in ItemModel.query.all()]}
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items"
        # result = cursor.execute(query)
        # items = []
        # for row in result:
        #     items.append({'name':row[0],'price':row[1]})

        # connection.close()

        # return {'items':items }
