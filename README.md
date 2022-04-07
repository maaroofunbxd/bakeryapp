
run the app after creating a k8s cluster (kind cluster) ```helm install myapp helm```

GET request at URL below produces the current items available

**localhost:5000/oven** - POST request in following JSON format: 
```
{"biryani":{
                "count": 10,
                "cost":  30
            }
}
```
also possible to run app using multiple containers in docker-compose ```docker-compose up```