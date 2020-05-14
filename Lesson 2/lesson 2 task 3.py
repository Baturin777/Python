numb_user = int(input("Введите номер месяца: "))
seasons_list = ["winter", "spring", "summer", "autumn"]
seasons_dir = {1 : "winter", 2 : "spring", 3 : "summer", 4 : "autumn"}
if numb_user == 12 or numb_user == 1 or numb_user == 2:
    print(seasons_dir.get(1))
    print(seasons_list[0])
elif 3 <= numb_user <= 5:
    print(seasons_dir.get(2))
    print(seasons_list[1])
elif 6 <= numb_user <= 8:
    print(seasons_dir.get(3))
    print(seasons_list[2])
elif 9 <= numb_user <=11:
    print(seasons_dir.get(4))
    print(seasons_list[3])
else:
    print("Такого месяца нет")