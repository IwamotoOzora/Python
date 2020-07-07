from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
import chromedriver_binary
from time import sleep

driver = webdriver.Chrome()
driver.get("https://a-force.biz/")

try:
    # チャットボットを出す
    search_chat_button = driver.find_element_by_id("button-area")
    search_chat_button.click()

    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    sleep(3)

    #チャットボットへ挨拶をする
    search_chat_form = driver.find_element_by_id("tweet")
    search_chat_form.send_keys("おはよう")
    search_send_button = driver.find_element_by_id("send_btn")
    search_send_button.click()

    sleep(3)

    # チャットボットへ質問する
    search_chat_form.send_keys("社風")
    search_send_button.click()

    sleep(5)

    # 質問の答えを出力する
    message = driver.find_elements_by_class_name("alert")[4].text 
    print(message)

finally:
    driver.quit()