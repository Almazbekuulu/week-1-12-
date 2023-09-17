
# Задача 1 .1
def add_excitement(spisok: list):
    spisok[:] = [i + "!" for i in spisok]


# Задача 1 .2
def add_excitement(spisok: list, newspisok: list):
    newspisok[:] = [i + "!" for i in spisok]
    return newspisok
# Задача 2
def match(str1:str,str2:str):
    b = 0
    for i in list(str1):
        if i in list(str2):
            if list(str1).index(i) == list(str2).index(i):
                b += 1
    return b

# Задача 3
def findall(stroka:str,symbol:str):
    indix = [i for i in range(0, len(list(stroka))) if stroka[i]== symbol]
    return indix




















#print(random.choice(spisok))
