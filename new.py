from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.maximize_window()

url = 'https://www.mensa.lu/en/mensa/online-iq-test/online-iq-test.html'

driver.get(url)

xpath_q1 = '//input[@name="q1"]'
q1_a = 'M'
q1 = driver.find_element('xpath', xpath_q1)
q1.send_keys(q1_a)
q1.send_keys(q1_a)
q1.send_keys(q1_a)
print(q1.text)

xpath_q9_a = '//input[@name="q9"][@value="a"]'  # //input[@name="q9" and @value="a"]
q9_a = driver.find_element('xpath', xpath_q9_a)
q9_a.click()

xpath_q19_a = '//input[@name="q19" and @value="a"]'
q19_a = driver.find_element('xpath', xpath_q19_a)
q19_a.click()

xpath_finish_button = '//input[@value="FINISHED"]'
finish_button = driver.find_element('xpath', xpath_finish_button)
finish_button.click()

textarea = driver.find_element('id', 'Result')
t = textarea.screenshot_as_png
f = open('screen.png', 'wb')
f.write(t)
f.close()

tt = driver.find_element('xpath', '/html/body/div/div/div/main/div[4]/div[2]/div/form/p[5]')
print(tt.text)
time.sleep(5000)
