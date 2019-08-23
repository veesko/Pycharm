from classesandobjects import AtmCard
joanCard = AtmCard('1234-4567-8999',45000,'78j','09/20','7545hjf')
# markCard = AtmCard()
# sharonCard = AtmCard()

# constructor method runs everytime we instantiate a class
print((joanCard.cvc))
print(joanCard.accNum)
print(joanCard.deposit(2000))
print(joanCard.checkBalance())
# print(joanCard.deposit(45000))
# print(joanCard.balance)
# print(joanCard.withDraw(100))
# print(joanCard.balance)