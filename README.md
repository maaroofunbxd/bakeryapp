
### App design
MVC pattern using flask blueprint and routes.

### Running the app
1. run the app after creating a k8s cluster (kind cluster) ```helm install myapp helm```
    
    portforward local port to access pods inside the cluster ```kubectl port-forward myapp-helm-xxxx 5000:5000``` 


2. also possible to run app using multiple containers in docker-compose ```docker-compose up```

### Requests to server

POST request to ```localhost:5000/oven```  is to be made with following JSON format body: 
```
{
  "biryani":{
                "count": 10,
                "cost":  30
            }
}
```
GET request to ```localhost:5000/oven```  lists the current items available