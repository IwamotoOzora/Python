from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_binary
from time import sleep

driver = webdriver.Chrome()
driver.get("https://a-force.biz/")

wait = WebDriverWait(driver, 10)

try:
    # チャットボットを出す
    open_chat_bot_element = driver.find_element_by_id("button-area")
    open_chat_bot_element.click()

    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    #チャットボットへ挨拶をする
    input_element = driver.find_element_by_id("tweet")
    input_element.send_keys("おはよう" + keys.ENTER)

    # チャットボットへ質問する
    element = wait.until(EC.presence_of_element_located((By.XPATH,\
         "//*[@id='field']/div[3]/div[2]/div[2]/div")))
    input_element.send_keys("社風" + keys.ENTER)

    # 質問の答えを出力する
    element = wait.until(EC.presence_of_element_located((By.XPATH,\
         "//*[@id='field']/div[5]/div[2]/div[2]/div")))
    message = driver.find_elements_by_class_name("alert")[4].text 
    print(message)

finally:
    driver.quit()