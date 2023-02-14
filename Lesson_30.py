from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

# url = 'https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html'
#
# driver.get(url)
#
# time.sleep(3)
#
# button_1 = driver.find_element('xpath', '//img[@alt="Lëtzebuergesch"]')
# button_1.click()
# time.sleep(2)
# button_2 = driver.find_element('xpath', '//img[@alt="Français"]')
# button_2.click()
# time.sleep(2)
# button_3 = driver.find_element('xpath', '//img[@alt="Deutsch"]')
# button_3.click()
# time.sleep(2)
# button_4 = driver.find_element('xpath', '//img[@alt="English (UK)"]')
# button_4.click()
# time.sleep(2)
#
# driver.close()

url = 'https://bank.gov.ua/ua/markets/exchangerates'
driver.get(url)
time.sleep(2)

f = open('currency.txt', 'wt')
# //tr/td[contains(text(),"CAD")]
# //tr/td[contains(text(),"CAD")]/parent::tr/td[contains(text(),",")]
xpath_name_can = '//tr/td[contains(text(),"CAD")]'
xpath_currency_can = '//tr/td[contains(text(),"CAD")]/parent::tr/td[contains(text(),",")]'
name_can = driver.find_element('xpath', xpath_name_can)
currency_can = driver.find_element('xpath', xpath_currency_can)

xpath_name_AUD = '//tr/td[contains(text(),"AUD")]'
xpath_currency_AUD = '//tr/td[contains(text(),"AUD")]/parent::tr/td[contains(text(),",")]'
name_AUD = driver.find_element('xpath', xpath_name_AUD)
currency_AUD = driver.find_element('xpath', xpath_currency_AUD)

xpath_name_AZN = '//tr/td[contains(text(),"AZN")]'
xpath_currency_AZN = '//tr/td[contains(text(),"AZN")]/parent::tr/td[contains(text(),",")]'
name_AZN = driver.find_element('xpath', xpath_name_AZN)
currency_AZN = driver.find_element('xpath', xpath_currency_AZN)

xpath_name_BGN = '//tr/td[contains(text(),"BGN")]'
xpath_currency_BGN = '//tr/td[contains(text(),"BGN")]/parent::tr/td[contains(text(),",")]'
name_BGN = driver.find_element('xpath', xpath_name_BGN)
currency_BGN = driver.find_element('xpath', xpath_currency_BGN)

xpath_name_HKD = '//tr/td[contains(text(),"HKD")]'
xpath_currency_HKD = '//tr/td[contains(text(),"HKD")]/parent::tr/td[contains(text(),",")]'
name_HKD = driver.find_element('xpath', xpath_name_HKD)
currency_HKD = driver.find_element('xpath', xpath_currency_HKD)

xpath_name_PLN = '//tr/td[contains(text(),"PLN")]'
xpath_currency_PLN = '//tr/td[contains(text(),"PLN")]/parent::tr/td[contains(text(),",")]'
name_PLN = driver.find_element('xpath', xpath_name_PLN)
currency_PLN = driver.find_element('xpath', xpath_currency_PLN)


c = f'{name_can.text} : {currency_can.text} \n{name_AUD.text} : {currency_AUD.text} \n{name_AZN.text} : {currency_AZN.text} \n{name_HKD.text} : {currency_HKD.text} \n{name_BGN.text} : {currency_BGN.text} \n{name_PLN.text} : {currency_PLN.text}'
print(c)
f.write(c)


f.close()
driver.close()
