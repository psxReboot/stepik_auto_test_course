from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):1
    return str(math.log(abs(12*math.sin(int(x)))))


browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser,10).until(EC.text_to_be_present_in_element((By.ID,'price'),'100'))
browser.find_element(By.ID,'book').click()

browser.find_element(By.ID,"answer").send_keys(calc(browser.find_element(By.ID,'input_value').text))
browser.find_element(By.ID,"solve").click()


