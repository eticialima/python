import requests 
import json 

SUBSCRIPTION_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxx"

vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"

address = vision_service_address + "analyze"
parameters  = {'visualFeatures':'Description,Color', 'language':'en'}
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()
headers    = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}

response = requests.post(address, headers=headers, params=parameters, data=image_data)
response.raise_for_status()
results = response.json()

print(json.dumps(results))
