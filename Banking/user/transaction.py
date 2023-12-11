import time


class transaction:
    def __init__(self, allUser):
        self.allUser = allUser

    def balance(self):
        cardNum = input("Please enter your account number: ")
        user = self.allUser.get(cardNum)
        if not user: 
            print("This account is not exited.")
            return  -1
        if user.card.cardLock:
            print("This account is locked down.")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("Wrong password. Your account is locked down...")
            user.card.cardLock = True
            return -1
        print("Account number：%s  Account balance：%d" % (user.card.cardId, user.card.cardMoney))
        
    def withdraw(self):
        cardNum = input("Please enter your account number: ")
        user = self.allUser.get(cardNum)
        if not user:
            print("This account is not exited.")
            return -1
        if user.card.cardLock:
            print("This account is locked down.")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("Wrong password. Your account is locked down...")
            user.card.cardLock = True
            return -1

        money = int(input("Please enter withdraw amount："))
        if money > user.card.cardMoney:
            print("Exceed account balance. Fail for withdraw..")
            return -1
        if money < 0:
            print("No avaliable account balance. Fail for withdraw...")
            return -1
        user.card.cardMoney -= money
        print("Withdraw success. Account banlance: %d" % (user.card.cardMoney))

    def deposit(self):
        cardNum = input("Please enter your account number: ")
        user = self.allUser.get(cardNum)
        if not user:
            print("This account is not exited.")
            return -1
        if user.card.cardLock:
            print("This account is locked down.")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("Wrong password. Your account is locked down...")
            user.card.cardLock = True
            return -1

        money = int(input("Please enter deposit amount："))
        if money < 0:
            print("Invalid amount. Fail for deposit...")
            return -1
        user.card.cardMoney += money
        print("Deposit success: %d Account balance: %d" % (money, user.card.cardMoney))

    def transfer(self):
        cardNum = input("Please enter your account number: ")
        user = self.allUser.get(cardNum)
        if not user: 
            print("This account is not exited.")
            return -1
        if user.card.cardLock:
            print("This account is locked down.")
            return -1
        if not self.checkPasswd(user.card.cardPasswd):
            print("Wrong password. Your account is locked down...")
            user.card.cardLock = True
            return -1

        money = int(input("Please enter transfer amount："))
        if money > user.card.cardMoney or money < 0:
            print("Invalid amount. Fail for transfer...")
            return -1
        newcard = input("Please enter the receive account number：")
        newcard = self.allUser.get(newcard)
        if not newcard:
            print("This account is not exited. Fail for transfer...")
            return -1
        if newcard.card.cardLock:
            print("This receive account is locked. Fail for transfer...")
            return -1
        user.card.cardMoney -= money
        newcard.card.cardMoney += money
        time.sleep(1)
        print("Transfer success")
        time.sleep(1)
        print("Transfer amount: %d Account balance %d" % (money, user.card.cardMoney))

    def checkPasswd(self, realPasswd):
        for i in range(3):
            tempPasswd = input("Please enter your password: ")
            if tempPasswd == realPasswd:
                return True
        return False