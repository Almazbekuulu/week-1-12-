# Создайте симулятор магазина, включая классы Product, Customer, Cart и Store.
# Класс Product должен иметь атрибуты, такие как название, цена и количество на складе.
# Класс Customer представляет клиента и имеет атрибут cart для добавления товаров.
# Класс Store управляет инвентарем и покупками.
# Реализуйте функциональность добавления товаров в корзину, расчет общей суммы и обновление инвентаря.
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def addkart(self, product, quantity):
        self.cart.append((product, quantity))

class Cart:
    def __init__(self):
        self.items = []

    def total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

class Store:
    def __init__(self):
        self.inven = {}

    def add_product(self, product):
        if product.name in self.inven:
            self.inven[product.name].quantity += product.quantity
        else:
            self.inven[product.name] = product

    def purchase(self, customer):
        for product, quantity in customer.cart:
            if product.name in self.inven and self.inven[product.name].quantity >= quantity:
                self.inven[product.name].quantity -= quantity


#Создайте приложение для управления задачами. Реализуйте классы Task, TaskList, и User. Task должен иметь атрибуты, такие как название, описание и статус (выполнено/не выполнено). TaskList содержит список задач, и методы для добавления, удаления и фильтрации задач. Класс User хранит информацию о пользователях и их списки задач. Реализуйте возможность регистрации и авторизации пользователей.
class Task:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

class TaskList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def filter_tasks(self, status):
        return [task for task in self.tasks if task.completed == status]

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.task_lists = {}

    def create_task_list(self, list_name):
        if list_name not in self.task_lists:
            self.task_lists[list_name] = TaskList()


    def delete(self, list_name):
        if list_name in self.task_lists:
            del self.task_lists[list_name]

    def login(self, password):
        return self.password == password

    def __str__(self):
        return f"Пользователь: {self.username}, Списки задач: {', '.join(self.task_lists.keys())}"

