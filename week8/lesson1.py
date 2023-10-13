#Создайте класс Playlist, представляющий плейлист с песнями. Переопределите метод __str__, чтобы он выводил список песен в читаемом виде, и метод __len__, чтобы можно было узнать количество песен в плейлисте.
class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)



    def __str__(self):
        return "\n".join(self.songs)

    def __len__(self):

        return len(self.songs)


ss = Playlist()
ss.add_song("cghf")
ss.add_song("hfghgh")
ss.add_song("ghfhgh")


print(ss)

print(f"Количество : {len(ss)}")

#Создайте класс, который будет представлять собой неизменяемый объект, и переопределите методы __hash__ и __eq__, чтобы можно было использовать его в множествах и как ключи в словарях.
class Set:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Set):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):

        return hash((self.x, self.y))

    def __str__(self):
        return self.x ,self.y

o1 = Set(1, "A")
o2 =Set(2, "z")
o3 = Set(4, "cc")
o4 = Set(4, "cc")#он не отобразится  потому что дубликат сет не принимает


my_set = {o1.__str__(), o2.__str__(), o3.__str__(),o4.__str__()}
print(my_set)
