# Parent Class
class User():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        

    def show_details(self):
        try:
            print("")
            print("------------------------")
            print("")
            print("User Details")
            print("Name        :",self.name)
            print("Age         :",self.age)
            print("Gender      :",self.gender)
        except Exception as e:
            print(e)

# Child Class
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0
        self.details()
        self.enquiry()
        
        while self.user > 0:
            if self.user == 1:
                self.balance_enquiry()
                self.details()
                self.enquiry()
            elif self.user == 2:
                self.deposite_amount = int(input("Deposite Amount: Rs. "))
                self.deposite(self.deposite_amount)
                self.details()
                self.enquiry()
            elif self.user == 3:
                self.withdraw_amount = int(input("Withdraw Amount: Rs. "))
                self.withdraw(self.withdraw_amount)
                self.details()
                self.enquiry()
            elif self.user == 4:
                self.show_details()
                self.details()
                self.enquiry()
            elif self.user == 5:
                break
            
    
    def details(self):
        print("")
        print("------------------------")
        print("")
        print("For Balance Enquiry: 1")
        print("For Deposite       : 2")
        print("For Withdraw       : 3")
        print("For Account Details: 4")
        print("To Exit            : 5")
        print("")
        print("------------------------")
        print("")

    def enquiry(self):
        self.user = int(input("Enter here: "))

    def deposite(self,amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Your updated balance is: Rs. ",self.balance)

    def balance_enquiry(self):
        print("Your available balance is: Rs. ",self.balance)

    def withdraw(self,amount):
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficiant Balance. You're trying to withdraw: Rs. ",self.amount)
            print("You account balance is: Rs. ",self.balance)
        else:
            print("You have successfully withdraw: Rs. ",self.amount)
            self.balance = self.balance - self.amount
            print("Your updated balance is: Rs. ",self.balance)

name = input("Enter your name: ")
age = int(input("Enter your age: "))
gender = input("Enter your gender: ")

rohit = Bank(name,age,gender)

