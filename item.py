import sqlite3
from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
class Item(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument('price',type=float,required=True,help="this field can't be left blank")
    
    @jwt_required()
    def get(self,name):
        connection=sqlite3.connect("data.db")
        cursor=connection.cursor()

        query="SELECT * FROM trips WHERE deperture_station=?" #OR arrival_station LIKE=?
        result=cursor.execute(query,(name,))
        row=result.fetchone()
        connection.close()
        
        if row:
            return {"trip":{"deperture_station":row[1] ,"arrival_station":row[2],"price":row[3]}}
        return {"message":"no trips for this place"},404
    
    def post(self,name):
        if next(filter(lambda x: x['name']==name,items),None) is not None:
            return {'message':"item with name '{}' already exists".format(name)},400
        request_data=Item.parser.parse_args()
        item={'name':name,'price':request_data['price']}
        items.append(item)
        return item,201
    def delete(self,name):
        global items
        items=list(filter(lambda x: x['name']!=name,items))
        return {'message':'item deleted'}
    def put(self,name):
        request_data=Item.parser.parse_args()
        item=next(filter(lambda x: x['name']==name,items),None)
        if item is None:
            item={'name':name , 'price':request_data['price']}
        else:
            item.update(request_data)
        return item
class ItemList(Resource):
    
    def get(self):
        return {'items':items}