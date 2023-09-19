#Задачи 1
def max_value(*args):
    return max(args)
#Задачи 2
def merge_lists(*args):
    x=[]
    i=0
    while i < len(args):
        x += args[i]
        i+=1
    return (x)
#Задачи 3
def print_user_data(**kwargs):
    for key, value in kwargs.items():
        print(key,':',value)

print_user_data(name="John", age=30, city="New York", occupation="Programmer")






