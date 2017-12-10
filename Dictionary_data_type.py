# Define a Dictionary
d = {'name':'Aadvik', 'age': 2, "phone":'999-999-9999'}
#print(d['name'])
#print(d['age'])

#get method
#print(d.get("name"))
#print(d.get("cources", 'Not found'))

# Update
d['courses']=['MAths','Physics','CompSc']

print(d)
d.update({'name': 'Aadvik Reddy','age': 3,'Prog_lang': 'Python'})

print(d)

#Len
#print(len(d))

#Delete
#del d["age"]
#print(d)

#POP
#d.pop("age")
#print(d)

#print(d.pop("age"))

#Keys

print(d.keys())

#Values
print(d.values())

#Items
print(d.items())

#for loop

for k,v in d.items():
 print(k,v)
