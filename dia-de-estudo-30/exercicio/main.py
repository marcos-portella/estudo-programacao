from accounts_ import Client, CurrentAccount, SavingsAccount, Bank

c1 = Client('Luiz', 30)
cc1 = CurrentAccount(111, 222, 0, 0)
c1.account = cc1
c2 = Client('Maria', 18)
cp1 = SavingsAccount(112, 223, 100)
c2.account = cp1
banco = Bank()
banco.clients.extend([c1, c2])
banco.accounts.extend([cc1, cp1])
banco.agencies.extend([111, 222])

if banco.authenticate(c1, cc1):
    cc1.deposit(10)
    c1.account.deposit(100)
    print(c1.account)
else:
    print('Não possível autenticar')  # depois temos que fazer uma lógica
