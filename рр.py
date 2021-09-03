from selenium import webdriver
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link =  'http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    chess = x_element.get_attribute('valuex')
    x = x_element
    y = calc(x)

    browser.find_element_by_id('answer').send_keys(str(y))
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option1 = browser.find_element_by_id("robotsRule")
    option1.click()
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:

    time.sleep(10)

    browser.quit()












