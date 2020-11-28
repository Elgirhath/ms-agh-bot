from selenium import webdriver
import logging

webdriverPath = "./data/chromedriver.exe"

WINDOW_SIZE = "1920,1080"

def get_driver():
    logging.info("Opening Chrome")
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    return webdriver.Chrome(webdriverPath, chrome_options=chrome_options)
