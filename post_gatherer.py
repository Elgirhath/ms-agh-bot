from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unidecode
from time import sleep
from datetime import datetime
import logging

SCROLL_PAUSE_TIME = 0.5

seen_posts = []

class Post:
    def __init__(self, author, time, message, comment_box):
        self.author = author
        self.time = time
        self.message = message
        self.comment_box = comment_box

    def comment(self, text, driver):
        actions = ActionChains(driver)

        scroll_up_to_element(driver, actions, self.comment_box)

        self.comment_box.click()
        actions.send_keys(text)
        actions.send_keys(Keys.RETURN)
        actions.perform()

    def get_normalized_message(self):
        asciidata=unidecode.unidecode(self.message) # discard polish characters
        return asciidata.lower()

def scroll_up_to_element(driver, actions, element):
    diff = driver.execute_script('return window.scrollY;') - element.location['y']
    while diff >= -500:
        driver.execute_script("window.scrollTo(0, window.scrollY - 100)")
        diff = driver.execute_script('return window.scrollY;') - element.location['y']

def get_posts(driver):
    logging.info('Gathering posts')

    # scroll multiple times to load feed
    for i in range(0, 10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(SCROLL_PAUSE_TIME)

    feed = driver.find_element_by_xpath("//*[@role='feed']")

    articles = feed.find_elements_by_xpath(".//*[@role='article']")

    posts = []

    for article in articles:
        try:
            post = create_post_from_article(article)

            is_new = True
            for saved_post in seen_posts:
                if post.author == saved_post.author and post.message == saved_post.message:
                    is_new = False
                    break

            if is_new:
                seen_posts.append(post)
                posts.append(post)

        except Exception as e:
            logging.info(e)

    return posts

def create_post_from_article(article_element):
    post = article_element.find_element_by_xpath("div/div/div/div/div/div[2]/div")

    info = post.find_element_by_xpath("div[2]/div/div[2]/div")
    author = info.find_element_by_xpath("div[1]").get_attribute('innerText')
    message = post.find_element_by_xpath("div[3]").get_attribute('innerText')
    comment_box = post.find_element_by_xpath("div[4]//form")
    time = datetime.now() #since time can't be taken from the post

    return Post(author, time, message, comment_box)