import time
import random
from .card import Card, User

class action(object):
    
    def __init__(self, allUser):
        self.allUser = allUser
        
    def createUser(self):
       
        name = input("Please enter your name:")
        idCard = input("Please enter your id: ")
        phone = input("Please enter your phone number")
        prestoreMoney = float(input("Please enter you prestore money："))
        if prestoreMoney <= 0:
            print("wrong prestore money....")
            return  -1

        
        firstPasswd = input("Please enter password：")
        secondPasswd = input("Please enter password again：")

        if firstPasswd != secondPasswd:
            print("not matched......")
            return -1
        print("Password set, please remember it: %s " % secondPasswd)
        
        cardId = self.randomCardId()
        card = Card(cardId, secondPasswd, prestoreMoney)
        user = User(name, idCard, phone, card)
        # save
        self.allUser[cardId] = user
        print("Create User Successfully！！Please remember the card number...(%s)" % cardId)
        
        
    
    def randomCardId(self):
        while True:
            str = ""
            for i in range(12):
                ch = chr(random.randrange(ord('0'), ord('9') + 1))
                str += ch
            if not self.allUser.get(str):
                return str
            
    def killUser(self):
        cardNum = input("Please enter card number：")
        # check card number
        user = self.allUser.get(cardNum)
        if not user:
            print("Not exist!")
            return -1

        # check password        
        if not self.checkPasswd(user.card.cardPasswd):
            print("Incorrect password!")
            return -1
        

        del self.allUser[cardNum]
        time.sleep(1)
        print("remove the user successfully！")
        
    def checkPasswd(self, realPasswd):        
        tempPasswd = input("Please enter password：")           
        if tempPasswd == realPasswd:
            return True
        return False
