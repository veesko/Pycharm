# #a class is a collection of related attributes, methodes, functions
# # class variables:- properties of a class
# class Student:
#     uniform = "red"
#     feeStatus = 0
#     def payFee(self): # a method of the class student
#         return "paid"
#
# # instantiate a class
# joan = Student()
#
# print(type(joan))
# print(joan.uniform)
#
# mark = Student()
# print(mark.payFee())

class AtmCard:
    cardNum = "xxxx-xxxx-xxxx"
    balance = 0
    cvc = "yyy"
    expDate = ""
    accNum = "abcdefg"


    def __init__(self,cardNum,balance,cvc,expDate,accNum):# this methods runs everytime we instantiate a class
        self.cardNumber = cardNum
        self.balance = balance
        self.cvc = cvc
        self.expiry = expDate
        self.accno = accNum


    def withDraw(self, amt):
        if self.balance <= amt:
            return "insufficient funds,your balance is,",self.balance
        else:
            self.balance -= amt
            return "withdrawal success, your balance is:", self.balance
        # pass #not sure of what to put in
    def deposit(self, amt):
        self.balance += amt
        return "deposit success",self.balance
    def checkBalance(self):
        return self.balance
