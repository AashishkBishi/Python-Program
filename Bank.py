class Bank():
    IFSC='BANK000024'
    ROI=0.07
    def __init__(self,name,accno,bal,mobno,pin):
        self.name=name
        self.accno=accno
        self.bal=bal
        self.mobno=mobno
        self.pin=pin
    def Details(self):
        print(f'Name={self.name}')
        print(f'Account number={self.accno}')
        print(f'Balance={self.bal}') 
    def WithDrawn(self):
        attempt=3
        while attempt >0:
            print(f'No of chances is {attempt}')
            if self.getpassword()==self.pin:
                amount=int(input('enter the amount to withdrawn'))
                if amount<= self.bal:
                    if amount % 100== 0:
                        if 100 <= amount <= 10000:
                            self.bal-=amount
                            print('Amount debited successfully......')
                            print(f'Available bal is {self.bal}')
                            break
                        else:
                            print('Enter valid amount')
                    else:
                        print('no denominations')    
                else:
                    print('In sufficient fund')    
            else:
                print('Invalid password')
                attempt-=1    
        else:
            print('no chances')  
            print('Try after 24 hours')  
    
    def Deposite(self):
        if self.accno ==int(input('enter account number:')):
            amount=int(input('enter the amount to deposited'))
            if amount % 100 ==0:
                if 100 <= amount <= 50000:
                    self.bal += amount
                    print('Amount credited successfully.....')
                    print(f'Available bal is {self.bal}')
                else:
                    print('Invalid amount')    
            else:
                print('Invalid denomination')    
        else:
            print('Invalid account number')
    def CheckBal(self):
        attemps=3
        while attemps >0:
            print(f'No of chances is{attemps}')
            if self.getpassword()==self.pin:
                print(f'Available bal is {self.bal}')
                break
            else:
                print('Invalid pin....')
                attemps-=1
                print('.........')
        else:
            print('No chances')
            print('Try after 24 hours')  
    @classmethod
    def changeROI(cls):
        cls.ROI=0.08          
    
    @staticmethod
    def getpassword():
        password=int(input('enter 4-digit pin='))
        return password
Cus1=Bank('User1',1234567890,10000,9876352676,1111)
Cus2=Bank('User2',1234560000,29999,9999999999,2222)
Cus3=Bank('User3',1234500000,50000,6565656565,3333) 
print(Cus1.CheckBal())   
