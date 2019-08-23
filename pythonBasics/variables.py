a = 10  #declaring variables
a=b=c=10
#print(b)
name = "joan"
# type checks the typ of variables
#print(type(name))
#boolean:- True, False

# conversion :- typecasting
distance = "10"
print(type(int(distance)))

#strings operations
fName = "joan"
sName = "wan"
print(len(fName))

#indexing
# TODO:explore all string methods
firstLetter = fName[0]
print(fName[0])
lastLetter = fName[len(fName)-1]
print(fName[-1])
print(fName.upper())
print(fName.count("o"))# finds all occurences of o


print(fName +" "+ sName)