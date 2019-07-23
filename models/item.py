# import sqlite3
from db import db


class ItemModel(db.Model):

    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):

        return cls.query.filter_by(name=name).first()  # SELECT * FROM items HERE name=name and return first row only
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()
        # connection.close()

        # if row:
        #     return cls(row[0], row[1])
        #     # return {'item':{'name':row[0],'price':row[1]}}   

    # def update(self):
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()

    #     query = "UPDATE items SET price=? WHERE name=?"
    #     cursor.execute(query, (self.name, self.price))

    #     connection.commit()
    #     connection.close()

    def insert(self):
        db.session.add(self)
        db.session.commit()

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()

        # query = "INSERT INTO items VALUES (?,?)"
        # cursor.execute(query, (self.name, self.price))

        # connection.commit()
        # connection.close()

        # # if next(filter(lambda x: x['name'] == name, items), None) is not None:
        # #     return {'message': "An item with name '{}' already exists.".format(name)}
        # data = Item.parser.parse_args()

        # # data = request.get_json()
        # item = {'name':name, 'price':data['price']}
        # items.append(item)
        # return item, 201 # Status code for Created        

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()    