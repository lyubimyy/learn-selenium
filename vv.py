from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'

try:
  browser = webdriver.Chrome()
  browser.get(link)
  1 + '0'
  x_element = browser.find_element_by_id("input_value")
  x = x_element.text
  y = calc(x)

  browser.find_element_by_id('answer').send_keys(str(y))


  option1 = browser.find_element_by_id("robotCheckbox")
  option1.click()
  option1 = browser.find_element_by_id("robotsRule")
  option1.click()
  button = browser.find_element_by_class_name("btn.btn-default")
  button.click()
except TypeError as e:
  raise e
finally:

    time.sleep(2)

    browser.quit()



