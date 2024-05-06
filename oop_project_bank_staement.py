import random

class User:
    def __init__(self, name, email, address, account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.total_loan = 0
        self.total_balance = 0
        self.count = 0
        self.transaction=[]
        self.account_num = self.generate_account_num()
        
    def generate_account_num(self):
        return random.randint(100000,777777)
    def deposit(self,amount):
        self.total_balance+=amount
        self.transaction.append(f'deposit:{amount}')
    def withdraw(self,amount):
        if amount>self.total_balance:
            print("Withdrawal amount exceeded")
        else:
            self.transaction.append(f'withdraw:{amount}')
            self.total_balance-=amount
    def available_balance(self):
        return self.total_balance
    def take_loan(self):
        if self.count<2:
            loan =int(input('Enter loan: '))
            self.total_loan+=loan
            self.count+=1
            self.transaction.append(f'take loan{loan}')

        else:
            print('Loan not possible.')
    def transfer_money(self,recip,amount):
        if self.total_balance>=amount:
            self.total_balance-=amount
            recip.total_balance+=amount
        else:
            print("not transfer.")

    def view_transactions(self):
        for transaction in self.transaction:
            print(transaction)

class Admin:
    def __init__(self):
        self.account_list={}

    def create_account(self,name,email,address,account_type,deposit):
        user = User(name, email, address, account_type)
        user.deposit(deposit)
        self.account_list[user.account_num]=user
    def delete_account(self, num):
        if num in self.account_list:
            del self.account_list[num]
        else:
            print('Account not match.')
    def show_account(self):
        if self.account_list:
            for num,user in self.account_list.items():
                print(f"Number:{num},Name:{user.name}")
        else:
            print('No account')
    def show_available_balance(self):
        total_balance =0
        for user in self.account_list.values():
            total_balance += user.available_balance()
        print(f"Total balance: {total_balance}")
    def show_loan(self):
        for num, user in self.account_list.items():
            print(f'Total Loan: {user.total_loan}')
    def loan_features(self):
        for user in self.account_list.items():
            if user.count>=2:
                print("Off")
            else:
                print("On")

admin = Admin()
run = True

while run:
    print('1. User:')
    print('2. Admin:')
    run1=True
    option=int(input('choice option:'))

    while run1:
        if option==1:
            print('1. Create account')
            print('2. Deposit money')
            print('3. Withdraw money')
            print('4. Take loan')
            print('5. Show loan features')
            print('6. Transfer money')
            print('7. Show accounts')
            print('8. show transaction:')
            print('9. Exit')
            options= int(input('option:'))
            if options==1:
                name=input('Enter name:')
                email= input('Enter email:')
                address=input('Enter address:')
                account_type=input('Enter account type:')
                deposit=int(input('Enter deposit:'))
                admin.create_account(name,email,address,account_type,deposit)
            elif options==2:
                num=input('Enter num:')
                money=int(input('Enter money:'))
                if num in admin.account_list:
                    admin.account_list[num].deposit(money)
                else:
                    print("Account not match")
            elif options==3:
                num = int(input('Enter number:'))
                money = int(input('Enter amount:'))
                if num in admin.account_list:
                    admin.account_list[num].withdraw(money)
                else:
                    print("Account not match")
            elif options==4:
                num=int(input('Enter account:'))
                if num in admin.account_list:
                    admin.account_list[num].take_loan()
                else:
                    print("Account not match")
            elif options==5:
                admin.loan_features()
            elif options==6:
                amount =int(input('Money:'))
                sender_email=input('sender_email:')
                recipient_email=input('recipt_email:')
                for account in admin.account_list.values():
                    if account.email==recipient_email:
                        account.transfer_money(sender_email,amount,account)
                        break
                else:
                    print("Recip email not match")
            elif options==7:
                admin.show_account()
            if options == 8:
                for user in admin.account_list.values():
                    user.view_transactions()
            elif options==9:
                run1 = False

        if option==2:
            print('1. Delete account:')
            print('2. Show available balance')
            print('3. Show loans')
            print('4. Exit')
            optionss=int(input('option:'))
            if optionss==1:
                num = int(input('account_num:'))
                admin.delete_account(num)
            elif optionss==2:
                admin.show_available_balance()
            elif optionss==3:
                admin.show_loan()
            elif optionss==4:
                run1 = False
