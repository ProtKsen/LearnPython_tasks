# Создайте словарь
my_dict = {"city": "Москва", "temperature": "20"}

# Выведите на экран значение ключа city
print(my_dict['city'])

# Уменьшите значение "temperature" на 5
my_dict['temperature'] = str(int(my_dict['temperature']) - 5)

# Выведите на экран весь словарь
print(my_dict)

# Проверьте, есть ли в словаре ключ country
print('country' in my_dict.keys())

#Выведите значение по-умолчанию "Россия" для ключа country
print(my_dict.get('country', 'Россия'))

# Добавьте в словарь элемент date со значением "27.05.2019"
my_dict['date'] = "27.05.2019"

# Выведите на экран длину словаря
print(len(my_dict))
