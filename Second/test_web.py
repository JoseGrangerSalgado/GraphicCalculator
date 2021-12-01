from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep, time
import random as r 



driver = webdriver.Chrome(executable_path='./chromedriver')


tests = [('x**2 - 49',r.randint(-100,100)), ('x^2 - 81',r.randint(-100,100)), ('x',r.randint(-100,100)), ('sin(x) + 11111',r.randint(-100,100)), ('cos(x+10)',r.randint(-100,100)), ('x/2 + 67.337182736',r.randint(-100,100)), ('log(x)',r.randint(-100,100)), ('x^4 - 40',r.randint(-100,100)), ('x**5 + 55',r.randint(-100,100)), ('log10(x) - 1',r.randint(-100,100))]

driver.maximize_window()

driver.get('http://127.0.0.1:5000/')
sleep(1)
with open('test_docs/selenium_test.txt', 'r+') as file:
    file.truncate(0)
    for test in tests:
        start = time()
        driver.find_element_by_id('text').send_keys(test[0])
        driver.find_element_by_id('x0').send_keys(test[1])
        driver.find_element_by_id('submit').click()
        driver.find_element_by_id('text').clear()
        driver.find_element_by_id('x0').clear()
        file.write(f"Test: {driver.find_element_by_id('test').text}, x0: {str(test[1])}\n")
        file.write(f"Root: {driver.find_element_by_id('result').text}\n")
        file.write(f"Message: {driver.find_element_by_id('message').text}\n")
        file.write(f"Precision: {driver.find_element_by_id('precision').text}\n")
        file.write(f"Time (ms): {driver.find_element_by_id('time').text}\n")
        file.write(f"Function Calls: {driver.find_element_by_id('calls').text}\n")
        end = time()
        file.write(f'Execution time: {end - start} seconds')
        file.write('\n\n')

driver.close()







# Documento Google Docs
# Variables Estadisticas


