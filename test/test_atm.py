
def get_pin():
    typed_pin = input('Please insert your pin code: ')
    return typed_pin


def test_get_pin(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda _:'123456')
    result = get_pin()
    assert result == '123456'


def withdraw_cash():
    money = int(input('Please insert the amount you want to withdraw: '))
    account_after_withdrawal = 100 - money
    return account_after_withdrawal


def test_withdraw_cash_with_right_amount(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda _:100)
    result = withdraw_cash()
    assert result >= 0

def test_withdraw_cash_with_excessive_amount(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda _:1000)
    result = withdraw_cash()
    assert result >= 0

def pin_authentication_and_withdraw():
    count = 0
    PIN='123456'
    while count < 3:
        typed_pin = get_pin()
        if typed_pin != PIN:
            count += 1
            print("incorrect password")
            return typed_pin
        else:
            withdraw_cash()
            return typed_pin


def test_correct_pin(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda _:'123456')
    result = pin_authentication_and_withdraw()
    assert result == '123456'


def test_incorrect_pin(monkeypatch):
    monkeypatch.setattr('builtins.input',lambda _:'wrongpassword')
    result = pin_authentication_and_withdraw()
    assert result == '123456'




