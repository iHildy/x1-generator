import time
import json
from RandomWordGenerator import RandomWord
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

reflink = input(
    'What is your referal link? (ex: https://x1creditcard.com/r/lFDs4Ml)')
rw = RandomWord(max_word_size=10)

class gen_class(object):

  def __init__(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
    # Step # | name | target | value
    # 1 | open | /?r=lFDs4Ml |
    self.driver.get(reflink)
    # 2 | setWindowSize | 1027x732 |
    self.driver.set_window_size(1027, 732)
    # 3 | click | css=.btn:nth-child(4) |
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(4)").click()
    # 4 | click | name=fname |
    self.driver.find_element(By.NAME, "fname").click()
    # 5 | type | name=fname | Firstq
    self.driver.find_element(By.NAME, "fname").send_keys(rw.generate())
    # 6 | type | name=lname | Last1
    self.driver.find_element(By.NAME, "lname").send_keys(rw.generate())
    # 7 | click | name=email |
    self.driver.find_element(By.NAME, "email").click()
    # 8 | type | name=email | rmail@email.com
    self.driver.find_element(By.NAME, "email").send_keys(rw.generate() + "@email.com")
    # 9 | click | css=.styles_root__2I3uR |
    self.driver.find_element(By.CSS_SELECTOR, ".styles_root__2I3uR").click()
    time.sleep(10)

# Instance created


# __call__ method will be called
while True:
    gen = gen_class()
    gen()
