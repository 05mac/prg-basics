class bank_account:

    def __init__(self, accountNo,):
        self.accountNo = accountNo
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Wpłaciłeś {amount}, teraz twoj stan konta to: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(
                f"Wypłaciłes {amount}, teraz twoj stan konta to: {self.balance:.2f}".replace('.',","))
        else:
            print("Za mało środków na koncie by wypłacić")

    def display_info(self):
        print(f"--------INFORMACJE---------")
        print(f"Numer Konta bankowego: {self.accountNo}")
        print(f"Twoje środki: {self.balance:.2f}".replace('.',","))
