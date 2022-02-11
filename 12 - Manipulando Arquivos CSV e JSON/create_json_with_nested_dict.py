import json

person_dict = {'first': 'Christopher', 'last':'Harrison'}
person_dict['City']='Seattle'

staff_dict ={}
staff_dict['Program Manager']=person_dict
staff_json = json.dumps(staff_dict)

print(staff_json)