import json
 
person_dict = {'first': 'Christopher', 'last':'Harrison'} 
person_dict['City']='Seattle' 
person_json = json.dumps(person_dict)
 
print(person_json)
