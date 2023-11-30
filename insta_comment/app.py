from time import sleep

import undetected_chromedriver as uc
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.heartless = False

driver = uc.Chrome()

driver.get('https://instagram.com')

wait = WebDriverWait(driver, timeout=5)

actions = ActionChains(driver)

sleep(5)

username = ''
password = ''
username_input = driver.find_element(By.XPATH, "//input[@name='username']")
password_input = driver.find_element(By.XPATH, "//input[@name='password']")
# submit_btn = driver.find_element(By.XPATH,"//button[contains(@class, '_acan') and contains(@class, '_acap') and contains(@class, '_acas') and contains(@class, '_aj1-') and contains(@class, '_ap30')]/div")


username_input.clear()
username_input.send_keys(username)

password_input.clear()
password_input.send_keys(password)

password_input.send_keys(Keys.ENTER)

print('cheguei')
sleep(10)

driver.get(
    ''
)


sleep(1000)
