import requests
from time import datetime

USERNAME = "MINH"
TOKEN ="Minh1611Minh1611Minh1611"
GRAPH_ID ="graph1"

pixela_endpoint = "https://pixe.la/v1/users"

users_params ={
    "token" :TOKEN,
    "user_name" :USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
    
}
# response=requests.post(url=pixela_endpoint,json = users_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/ {USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit":"Km",
    "type":"float",
    "color" : "ajisai",
}
headers ={
    "X-USER-TOKEN" : TOKEN

}
# response = requests.post(url= graph_endpoint,json=graph_config,headers=headers)
# print(response.text)
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs{GRAPH_ID}"

today = datetime(year=2023,month=7,day =21)
pixel_data ={
    "date":today.strftime("%Y%m%d"),
    "quantity":"10",
}
response = requests.post(url=pixel_creation_endpoint,json = pixel_data,headers=headers)
print(response.text)