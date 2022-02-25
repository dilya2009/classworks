#Loops - цикл

# 2 вида циклов:
#while
#for

# for i in range(20):
#     print(i, end=" ")


# range(stop) -> [0; stop)
# range(start, stop) -> [start;stop)
# range(start, stop, step)
 
# for i in range(200, 99, -2):
#     print(i, end=" ") 

# for i in range(1, 11):
#     print(f"9 х {i} = {9 * i}")

# def print_mult_table(num,up_to):
#     for i in range(1, up_to + 1):
#         print(f"{num} x {i} = {num * i}")


# def print_exp_table(num, up_to):
#     for i in range(from_num, up_to + 1):
#         print(f"{num} ** {i} = {num **i}")

# print_exp_table(44, 7, 13)

# for i in range(5, 10):
#     print(i/10)

# for i in range(2, 10, -1):
#     print(i)
# ! один проход цикла - итерация
# интерации можно пропускать с помощью слова continue
# for letter in "Dilnura":
#     if letter == " ":
#         break
#     else:
#         print(letter, end = " ")
    #print(letter, end="*")("*\n")
      

# print("Elbek" .upper())
# print("Elbek" .lower())
# print("E" .isupper())
# print("Elbek" .upper().isupper())
# print("123E" .isdigit())

new_str = ""
for letter in "Dilnura Abdukadirovanis a student":
   new_str = new_str + letter.swapcase()
print(new_str)









