# RESTapi
RESTapi to calculate sum, average and standard deviation. This project has been implemented in Python 3.8 and Docker.

## Installation
It requires docker to be installed in your system.
Refer to the official documentation on how to install docker: https://docs.docker.com/engine/install/ubuntu/

## Build
Clone this repository using 
```
git clone https://github.com/Voldemort175/RESTapi.git 
```

Then navigate to the cloned repository using cd.
Build the docker image using 
```
docker build -t ANY_TAG .
```
and then run the container using
```
docker run -d -p 8080:8080 ANY_TAG:latest
```
The uvicorn server is running now and you can send POST and GET requests.

## Usage 
Send POST requests of the numbers you want to store
```
curl -X POST http://localhost:8080/numbers?new=12
```
NOTE: Only integer values are allowed to be enetered. Any other value will result in an error

After multiple POST requests, you can calculate the sum, average or standard deviation by:
 ```
curl -X GET http://localhost:8080/numbers?sum
```
```
curl -X GET http://localhost:8080/numbers?average
```
```
curl -X GET http://localhost:8080/numbers?stddev
```
The resut will give you the answer.
 
