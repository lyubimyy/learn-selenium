from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_class_name('')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_class_name('form-control.third')
    input2.send_keys("prokop.tyy")
    input3 = browser.find_element_by_css_selector('div.second_block > div.form-group.first_class > input')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_css_selector('div.form-group.second_class > input')
    input4.send_keys("Russia")
    button = browser.find_element_by_class_name("btn.btn-default")
    button.click()

finally:

    time.sleep(30)

    browser.quit()