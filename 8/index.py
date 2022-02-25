# def draw_christmas_tree(size):
#     for i in range(1,  size + 1):
#         print("*" * i)

# draw_christmas_tree(5)

# def draw_rectangle(width, height):
#     for i in range(height):
#         print("*" * width)

# draw_rectangle(5, 2)
 
 #for i is upper

def clear_text_from_uppercase(text):
    for letter in text:
        new_text = ""
        if letter.isupper(): pass
        else: new_text = new_text + letter
    return new_text

print(clear_text_from_uppercase("HeLLo"))

def show_devisiors(divider):
    for i in range(divider):
        print(24 % divider)

show_devisiors(24)
#this is homework

