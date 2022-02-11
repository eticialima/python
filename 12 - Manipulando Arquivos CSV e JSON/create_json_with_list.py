import json

person_dict = {'first': 'Christopher', 'last':'Harrison'}
person_dict['City']='Seattle'

languages_list = ['CSharp','Python','JavaScript']

person_dict['languages']= languages_list

person_json = json.dumps(person_dict)

print(person_json)