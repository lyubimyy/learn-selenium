from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1')
    num2 = browser.find_element_by_id('num2')

    x = (int(num1))
    y = (int(num2))

    def sum(x, y):
     return str(x + y)

    select = Select(browser.find_element_by_id("dropdown")
    select.select_by_value('1')
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:

    time.sleep(30)

    browser.quit()
