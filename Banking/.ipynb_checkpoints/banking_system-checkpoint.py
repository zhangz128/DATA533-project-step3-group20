import time
import os
import pickle

from Banking.userside.userview import Userview
from Banking.adminside.verification import Vertifyadmin
from Banking.adminside.action import *
from Banking.userside.account import Account
from Banking.userside.transaction import Transfer

from Banking.card import Card
from Banking.user import User
  

class HomePage():
    def __init__(self):
        self.allUserD = {}  
        self.adminaction = adminaction(self.allUserD)
        self.account = Account(self.allUserD)
        self.transaction = Transfer(self.allUserD)
    def saveUser(self):
        self.allUserD.update(self.adminaction.allUser)
        self.allUserD.update(self.account.allUser)
        self.allUserD.update(self.transaction.allUser)
        
        absPath = os.getcwd()
        filepath = os.path.join(absPath, "allusers.txt")
        with open(filepath, "w") as txt_file:
            for user_id, user_data in self.allUserD.items():
                txt_file.write(f"{user_id}: {user_data}\n")
        
        print("Save successfully")
        
    def main(self):
        absPath = os.getcwd()
        filepath = os.path.join(absPath, "allusers.txt")
        try:
            with open(filepath, "rb") as f:
                allUser = pickle.load(f)
                print(allUser)
        except FileNotFoundError:
            allUser = {}
        
        self.adminaction = adminaction(self.allUser)
        self.account = Account(self.allUser)
        self.transaction = Transfer(self.allUser)
        
            
        while True:
            print("1. User")
            print("2. Admin")
            print("3. Quit")
            identity = input("Choose your identity: ")

            if identity == "1":
                view = Userview()
                view.printUserView()
                if view.userLong():
                    return -1

                while True:
                    view.printuserFunctionView
                    option = input("Please enter your action：")
                    if option == "1":   
                    #  deposit
                        self.transaction.saveMoney()

                    elif option == "2":
                    #  withdraw
                        self.transaction.getMoney()

                    elif option == "3":
                    #  transfer
                        self.transaction.transferMoney()

                    elif option == "q":
                        if not (self.view.userLong()):
                            self.saveUser()
                            print('Exit system')
                            return -1 

            elif identity == "2":

                # 界面对象
                view = Vertifyadmin()
                #  开机界面
                view.printAdminView()
                #  判断如果返回值为-1，就结束整个主程序
                if view.adminLong():
                    return -1

                while True:
                    view.printsysFunctionView()
                    option = input("Please enter your action：")
                    if option == "1":   
                    #  Create User
                        self.adminaction.createUser()

                    elif option == "2":
                    #  Deactivate 
                        self.adminaction.killUser()

                    elif option == "q":
                        if not view.adminLong():
                            self.saveUser()
                            print('Exit system')
                            return -1 

            elif identity == "3":   
                print("Quitting the program.")
                return 0

            else:
                print("Incorrect input. Please enter 1, 2, or 3.")

            
                
            
if __name__ == "__main__":
    homepage = HomePage()
    homepage.main()