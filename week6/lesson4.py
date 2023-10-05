class BankAccount:
    interest_rate = 0
    def deposit(self,balance,stavka):
        self.interest_rate = balance+stavka
        return self.interest_rate
    def withdraw(self,balance,stavka):
        self.interest_rate = balance-stavka
        return self.interest_rate

x = BankAccount()
print(x.deposit(12,3))
print(x.withdraw(12,3))

class Rectangle:
    height = 0
    width = 0

    def calculate_area(self,width,height):
        return width*height


s = Rectangle()
print(s.calculate_area(2,4))
class Counter:
    count=0


    def increment(self,x):
        self.count =self.count+x
        return self.count

    def decrement(self,x):
        self.count = self.count - x


        return self.count

m = Counter()
print(m.increment(1))
print(m.increment(1))
print(m.decrement(4))
print(m.increment(2))

















