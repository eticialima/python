import requests
import json

vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"
address = vision_service_address + "analyze" 
parameters  = {'visualFeatures':'Description,Color', 'language':'en'} 
subscription_key = "xxxxxxxxxxxxxxxxxxxxxxx" 
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, 'rb').read()
headers    = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': subscription_key}
 
response = requests.post(address, headers=headers, params=parameters, data=image_data)
response.raise_for_status() 
results = response.json()

print(json.dumps(results)) 
print()
print('all tags')
for item in results['description']['tags']:
    print(item)

print()
print('first_tag')
print(results['description']['tags'][0])


