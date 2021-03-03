import getpass
import logging
from datetime import datetime, timedelta
from time import sleep

import driver_util
import facebook_logger
import game_action
import game_action_controller
import game_action_selector
from data_extraction import game_data_extractor
import post_gatherer


def main(args):
    logging.basicConfig(filename="logs.txt",
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

    email = args["email"]
    password = args["password"]

    driver = driver_util.get_driver()

    facebook_logger.log_in(driver, email, password)

    group_url = args["group_url"]

    logging.info("Opening group url: " + group_url)
    driver.get(group_url)

    sleep(0.5)

    today = datetime.today().timetuple()

    first_check = True
    game_found = False

    action_controller = game_action_controller.GameActionController(driver, args)
        
    while not game_found:
        driver.refresh()

        posts = post_gatherer.get_posts(driver)

        logging.info(f"New posts: {len(posts)}")

        if not first_check:
            for post in posts:
                game_data = game_data_extractor.extract_game_data(post)

                action = game_action_selector.get_action(game_data, args)
                
                if action == game_action.IGNORE:
                    continue

                if action == game_action.NOTIFY:
                    action_controller.notify(post, game_data)

                if action == game_action.COMMENT:
                    action_controller.comment(post, game_data)
                    game_found = True

        first_check = False

        logging.info("Sleeping...")

        sleep(args["refresh_rate"])

        logging.info("Refreshing...")

    driver.quit()
