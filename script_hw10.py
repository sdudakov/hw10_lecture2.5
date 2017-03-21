
# заготовка для домашней работы
# прочитайте про glob.glob
# https://docs.python.org/3/library/glob.html

# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции
# на зачёт с отличием, использовать папку 'Advanced Migrations'

import glob
import os.path

def get_files():
	migrations = 'Migrations'
	sql_files = glob.glob(os.path.join(migrations, "*.sql"))
	return sql_files

def search_str_in_file(search_str, files):
	file_list = [] #создаю пустой список для имен файлов с найденной строкой
	file_sum = 0
	for current_file in files:
		with open(current_file, "r", encoding="utf-8") as file:
			for lines in file:
				line = file.readline()
				if search_str in line:
					file_sum += 1
					print(current_file)
					file_list.append(current_file) #на каждой итерации добавляю в список имя файла
	print("Всего: {}" .format(file_sum)) 
	return file_list

def search_input(): # функция осуществляющая вывод строки поиска
	search_str = str(input("Введите строку поиска:"))
	return search_str

def search_cycle():
	search_str = search_input()
	files = get_files()
	while True:
		files = search_str_in_file(search_str, files)
		search_str = search_input()

search_cycle()
