#1.  Создайте систему классов для электронной библиотеки.
# У вас должен быть базовый класс Item для представления элементов библиотеки (например, книг и видео),
# с атрибутами, такими как title, author, и year. Создайте подклассы для разных типов элементов
# (например, Book и Video), которые будут наследовать от базового класса Item.
# Реализуйте инкапсуляцию, чтобы контролировать доступ к атрибутам,
# и добавьте методы для вывода информации о каждом элементе.

class Item:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
    def info(self):
        print("Title:",self.__title,"\nAuthor:",self.__author,"\nYear:",self.__year)

class Book(Item):
    def __init__(self,title, author, year):
        super().__init__(title, author, year)

class Video(Item):
    def __init__(self,title, author, year):
        super().__init__(title, author, year)

video1ex = Video("lesson","teacher",2023)

video1ex.info()

book1ex = Book("math","mahmud",1992)

book1ex.info()
#2.
# Создайте систему классов для представления заказов в интернет-магазине.
# Создайте класс Product с атрибутами, такими как name, price, и quantity.
# Затем создайте класс Order, который может содержать несколько
# экземпляров Product. Реализуйте методы для добавления и удаления товаров
# из заказа, а также для вычисления общей суммы заказа.

class Product:

    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity




class Order(Product):
    def __init__(self,name, price, quantity):
        super().__init__(name, price, quantity)
    def total(self):

        print(self.price * self.quantity)


    def add(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


    def delete(self):
        self.name = None
        self.price = None
        self.quantity = None
product1 = Order('ex1',3,5)
product1.delete()
product1.add("ex",3,4)
product1.total()


print(product1.__dict__)
























