import redis
#import json
import os
r = redis.Redis(host=os.environ['REDIS_HOST'], port=6379)

class Model:  

    def getall(self):
        allitems = []
        for key in r.scan_iter(_type='HASH'):
            allitems.append(key.decode("utf-8"))
        return allitems

    def setitem(self,key,data):
        for i,j in enumerate(data[key]):
            r.hset(key,j,data[key][j])
        count=r.hget(key,"count").decode("utf-8")
        cost=r.hget(key,"cost").decode("utf-8")
        return count,cost

    def getitem(self,item):
        if r.exists(item)==0:
            return -1,-1
        return r.hget(item,"count").decode("utf-8"),r.hget(item,"cost").decode("utf-8")

    def deleteitem(self,item):
        if r.exists(item)==0:
            return -1
        r.delete(item)
        return 0

