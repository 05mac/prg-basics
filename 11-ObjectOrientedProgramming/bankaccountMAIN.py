from BankAccount import bank_account

my_account = bank_account("12 3456 5555 9090 1111 0000 7722")
my_account.display_info()
my_account.deposit(25.30)
my_account.display_info()
my_account.withdraw(31.70)
my_account.display_info()
my_account.withdraw(14)
my_account.display_info()