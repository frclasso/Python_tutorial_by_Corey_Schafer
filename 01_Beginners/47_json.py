#!/usr/bin/env python 3

import json

people_string = '''
{
    "people":[
        {
            "name": "John Smith",
            "phone": "555-615-88888",
            "emails": ["johnsmith@email.com","john.smith@company.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-77777",
            "emails": null,
            "has_license": true
        
        }       
    ]
}
'''
data = json.loads(people_string)
#print(data)
#print(type(data))

# for person in data['people']:
#     #print(person)
#     print(person['name'])

# descomente o codigo abaixo
for person in data['people']:
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)

