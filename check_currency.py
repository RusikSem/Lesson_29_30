from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://bank.gov.ua/ua/markets/exchangerates'
driver.get(url)
driver.maximize_window()
time.sleep(3)
f = open('currency.txt', 'wt')

xpath_currency_code = '//tr/td[contains(text(),"")][2]'
xpath_currency_value = '//tr/td[contains(text(),",")]'

codes = driver.find_elements('xpath', xpath_currency_code)
values = driver.find_elements('xpath', xpath_currency_value)
length_code = len(codes)

for i in range(length_code):
	c = f'{codes[i].text} : {values[i].text}'
	print(c)
	f.write(c)
	f.write('\n')

f.close()
driver.close()
