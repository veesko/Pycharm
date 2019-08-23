#Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No".
# b = input()
# if b == "yes" or b == "YES" or b == "Yes":
#     print("Yes")
# else:
#     print("No")
#
# # 2 Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max () function!
# par1 = int(input("Enter first value: "))
# par2 = int(input("Enter second value: "))
# par3 = int(input("Enter third value: "))
# def printMax (a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > c:
#         return b
#     else:
#         return c
#
# print("the Largest number is: "+ str(printMax(par1,par2,par3)))
#

#3 Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function
# def makeList(a = [], l =[]):
#       l.append(a[0])
#       l.append(a[-1])
#       return l
#
# finalList = makeList(a = [0,1,2,56])
# print(finalList)

# def makeList(numList):
#     newList = [numList[0],numList[-1]]
#     return newList
#
# list1 = input("Enter your list: ")


#print(makeList(list))

#
#
# #4.Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# # Hint: how does an even / odd number react differently when divided by 2?

#With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
# write a program to print the first half values in one line and the last half values in one line.
a = (1,2,3,4,5,6,7,8,9,10,12)
a1 = a[:int(len(a)/2)]
print(a1)





