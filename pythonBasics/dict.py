a = {}
#typecasting use dict

#print(type(a))
person = {"name":"joan","age":56,"city":"kisumu","phone":"0720222555"}
print(person["city"])
#print(person)

person2 = {"name":["joan","lea",{"anotherPsn":"han"}],"age":56,"city":"kisumu","phone":"0720222555"}
print(person2["name"][2]["anotherPsn"])

person2["age"] = {"young":10,"old":40}
print(person2)



# TODO: read dict methods

