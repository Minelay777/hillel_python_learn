# Спросить у пользователя год рождения.
age = input("Введите свой год рождения: ")

# Проверяем ввёл текст или число пользователь

if age.isdigit():
	age=int(age)
	
else :					# если нет - то просим ввести снова
	print("надо ввести число ")
	age = input("Введите свой год рождения: ")
	age = int(age)

# Если 21 год вывести “You should visit Holland.”

if (2022 - age) == 21:
	print("You should visit Holland.")

# Если больше 21 вывести “You should visit Vietnam.”

elif (2022 - age) > 21:
	print("You should visit Vietnam.")

# Все остальные варианты. Вывести “Travell everywhere”

else:
	print("Travell everywhere")
