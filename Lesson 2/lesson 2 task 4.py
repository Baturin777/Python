words = input("Введите несколько слов: ")
list_word = words.split()
for count, el in enumerate(list_word, 1):
    if len(el) > 10:
        el = el[0:10]
    print(f"{count} : {el}")
