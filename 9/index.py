# инициализация переиенной 
# while условие:
   # тело цикла

# ! В цикле while условие когда-то должно стать FALSE
# ? В условии есть переменная, которая доллжна меняться при каждым проходе цикла
# * Переменная меняется в целе цикла 
# ! Обычно переменная является счетчиком 

# Пример вывода чисел от 10 до 20 включительно
# i = 10
# while i <= 20:
#     print(i)
#     i = i + 1



# for i in range(10, 21):
#     print(i, end=" ")


# Пример вывода чисел от 200 до 150 включительно, десяткам

# for i in range(200, 149, -10):
#     print(i, end=" ")

# i = 200
# while i <= 150:
#     print(i, end=" ")
#     i = i - 10

#name = "Dilnura! This is my name"

# Индексы должны быть целым числомб, а иначе будет ошибка

# i = 0
# while i < 7:
#     print(name[i], end="/") 
#     i = i + 1

# for ltr in name:
#     print(ltr, end="/")

# for i in range(len(name)):
#     print(name[i], end="/")


# Способы создать бесконечный цикл
# 1. Написать условие,  которое всегда будет верным

# while 1 > 0:
#     pass


# # 2. В условии написать  True

# while True:
#     pass 

# Как остановить цикл, который бесконечный -> Нужно, чтобы консоль была активной и нажать Ctrl + C


# Как управлять циклом, который бесконечный?
# Ответ -> с помощью if  и break

# i = 0 
# while True:
#     print("Dilnura")
#     i = i + 1
#     if i == 10:
#         break


# while True:
#     num = int(input("Enter positive number: "))
#     if num < 0:
#         break

# int
# float
# bool

# !Индексируемые объекты
# str
# list

#Гомогенный список -> потому, что в нем только СТРОКИ
# students = ["Umar", "Abduvali", "Oybek", "Iskander"]
# ages = [16, 16, 16, 13, 14, 15]
# countries = ["Uzbekistan", "USA", "Poland", "Sweden"]
# country_codes = ['UZ', 'PO', 'UK', 'UA']

animals = ['elephant', 'horse', 'lion', 'tiger']
cities = ['Florida', 'Istanbul', 'Los-Angeles', 'New-York']
actors = ["Aidan Gallagher", 'Milley Bobby Brown', 'Noah Shnap']
drinks = ['Fanta', 'Coca-cola', 'Pepsi']
sweets = ['Snickers', 'Nutella', 'Mars', 'Nesquik']
peoples = ['Russian', 'Uzbek', 'American']
marvels = ['Spider-man', 'Iron-man', 'Capitan-America']
names = ['Stormi', 'West', 'Taylor']
Kardashians = ['Kendall', 'Kyeli', 'Khloe', 'Kourtney', 'Kim']
Brands = ['Gucci', 'Chanel', 'Prada', 'Hermes', 'Victorias Secret']











# i = 21
# while i <= 50:
#     print(i)
#     i = i + 1


