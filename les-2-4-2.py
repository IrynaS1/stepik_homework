from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser,12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    btn = browser.find_element(By.CSS_SELECTOR, value="#book")
    btn.click()
    numv = browser.find_element(By.CSS_SELECTOR, "#input_value")
    browser.execute_script("return arguments[0].scrollIntoView(true);", numv)
    x = int(numv.text)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, value="#answer")
    input.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()