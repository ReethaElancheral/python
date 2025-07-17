from banking.account_module import deposit, withdraw


def transfer(amount):
    withdraw(amount)
    deposit(amount)

