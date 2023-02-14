class Mobile:
	color = 'grey'
	mob_os = 'Android'
	ram = '4'
	storage = '64'

	@staticmethod
	def change_default_color(color):
		Mobile.color = color

	def __init__(self, color, system):
		self.color = color
		self.mob_os = system

	def show_ram(self):
		return self.ram

	def change_ram(self, new_ram):
		self.ram = new_ram

	def show_storage(self):
		return self.storage

	def change_storage(self, new_storage):
		self.storage = new_storage

	def __str__(self):
		return f'color: {self.color}, ram: {self.ram}, storage: {self.storage} '


xiaomi = Mobile('red', 'arm64')
print(xiaomi.show_ram())
xiaomi.change_ram('6')
print(xiaomi.show_ram())
print(xiaomi.color)
print(xiaomi.mob_os)

nokia = Mobile('green', 'arm64')
print(nokia.show_ram())

nokia.change_ram('128')
print(nokia.show_ram())
print(nokia.color)
print(Mobile.color)
print(nokia.mob_os)

print(xiaomi)
Mobile.change_default_color('yellow')
print(Mobile.color)

# '''Задание 3
# Создайте класс «Страна». Необходимо хранить
# вполях класса: название страны, название континента,
# количество жителей в стране, телефонный код страны,
# название столицы, название городов страны. Реализуйте
# методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса'''
#
#
# class Country:
# 	name_country = 'Ukraine'
# 	name_continent = 'Europa'
# 	residents = '40 000 000'
# 	telephone_code = '38097'
# 	capital = 'Kiev'
# 	country_cities = 'Odessa, Nikolaev, khercon'
#
# 	def chow_residents(self):
# 		return self.residents
#
# 	def change_residents(self, new_residents):
# 		self.residents = new_residents
#
# 	def __init__(self, telephone_code):
# 		self.telephone_code = telephone_code
#
# 	def __str__(self):
# 		return f'name_country - {self.name_country}\nname_continent - {self.name_continent}\nresidents - {self.residents}\ntelephone_code - {self.telephone_code}\ncapital - {self.capital}\ncountry_cities - {self.country_cities}'
#
# 	def add_city(self, add_city):
# 		self.country_cities = self.country_cities + ', ' + add_city
#
# 	def cities(self):
# 		return self.country_cities
#
#
# history = Country('38063')
# print(history.telephone_code)
# history.change_residents('30 000 000')
# print(history.chow_residents())
# print(history.name_country)
# print(history.name_continent)
# print(history)
# history.add_city('Lviv')
# print(history.cities())

