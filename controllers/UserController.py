from flask import render_template, redirect, url_for, request, abort, jsonify
from models.Model import Model

def bakeryinventory():
    allitems = Model().getall() 
    return jsonify( allitems )

def addtomenu():
    data = request.get_json()
    key=list(data.keys())[0]
    count,timetaken=Model().setitem(key,data)
    return ("item:{} count {} cost {}".format(key,count,timetaken))

def itemavailablty(item):
    #check if can be added condition of not existing
    count,cost=Model().getitem(item)
    if (count,cost)==(-1,-1):
        return "sorry"
    return jsonify({"count":count,"cost":cost})
    
def removeitem(item):
    Model().deleteitem(item)
    return "{} DELETED from bakerybase".format(item)


