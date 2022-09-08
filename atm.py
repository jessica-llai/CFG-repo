
class ATM:
    def __init__(self):
        self.PIN = '123456'
        self.ACCOUNT_BALANCE = 100
        self.count = 0

    def get_pin(self):
        typed_pin = input('Please insert your pin code: ')
        return typed_pin

    def withdraw_cash(self):
        print(f"Your current balance: {self.ACCOUNT_BALANCE}")
        withdraw_amount = int(input('Please insert the amount you want to withdraw: '))
        try:
            self.ACCOUNT_BALANCE = self.ACCOUNT_BALANCE - withdraw_amount
            assert self.ACCOUNT_BALANCE >= 0
        except AssertionError:
            print(f"insufficient balance")
        else:
            print(f"withdrew {withdraw_amount} successfully. Your remaining balance is {self.ACCOUNT_BALANCE}")

    def pin_authentication_and_withdraw(self):
        while self.count < 3:
            typed_pin = self.get_pin()
            if typed_pin != self.PIN:
                self.count += 1
                print("incorrect password")
            else:
                self.withdraw_cash()
                break


"""PLEASE ACTIVATE THE CODE TO RUN THE atm.py"""
# atm=ATM()
# atm.pin_authentication_and_withdraw()











