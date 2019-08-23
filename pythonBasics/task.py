taskList = [23, "jane",["lesson 23",560, {"currency": "kes"}],987,(76,"john")]
print(type(taskList))
print(taskList[2][2]['currency'])
print(taskList[2][1])
print(len(taskList))
list = list(taskList[-1])

print(list)
#print(taskList)
taskList[-2] = 789
print(taskList)




