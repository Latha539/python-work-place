#Dictionary
#1.dictionary example
d_name={"name": "Hema","age":"21","course":"python"}
print(type(d_name))

#2.Dictionary Operators
#Accessing values
d={"name":"Hema","age":21,"course":"python"}
print(d["name"])
print(d.get("age"))

#Different Between dict[key] and dict.get(key)
d={"name":"Hema","age":21,"city":"Nellore"}
print(d.get("course","Not available"))

#Adding and updating Items
d={"name":"Hema","age":21,"city":"Nellore"}
d["course"]="python"
print(d)


#3.Removing Items from a Dictionary
#Using pop()
details={"name":"hema","age":21,"branch":"ece","course":"python"}
age=details.pop("age")
print(age)
print(details)


#using del()
del details["course"]
print(details)

#Using popitems
details.popitem()
print(details)

#using cleary()
details.clear()
print(details)

#dict.update
d={"name":"hema","branch":"ece","course":"python"}
d.update({"age":21})
print(d)


#4.Functi0n for Dictionaries
#len()
d={"name":"hema","branch":"ece","course":"python"}
print(len(d))
#max()
print(max(d))
#min()
print(min(d))
#sorted()
print(sorted(d))

#6.Nested Dictionaries
students = {
"hema": {"age": 21,"course": "cs"},
"mahi": {"age": 22,"course": "math"}
}
print(students["hema"]["course"])
print(students["mahi"]["course"])