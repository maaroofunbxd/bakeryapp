from flask import request, jsonify
from models.Model import Model

def bakeryinventory():
    allitems = Model().getall() 
    return jsonify( allitems )

def addtomenu():
    data = request.get_json()
    key=list(data.keys())[0]
    count,cost = Model().setitem(key,data)
    return ("item ADDED:{} \n count:{} \n cost:{}".format(key,count,cost))

def itemavailablty(item):
    #GET the data of a particular item, from path "/oven/<item>"
    count,cost=Model().getitem(item)
    if (count,cost)==(-1,-1):
        return "item currently not available"
    return jsonify({"count":count,"cost":cost})
    
def removeitem(item):
    if (Model().deleteitem(item)==-1):
        return "item was not available to remove"
    return "{} DELETED from bakerybase".format(item)


