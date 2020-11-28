import logging
import winsound
import webbrowser
import ctypes

import email_notifier

class GameActionController:
    def __init__(self, driver, args):
        self.driver = driver
        self.args = args

    def notify(self, post, game_data):
        message = "Ta gra częściowo odpowiada twojemu zapytaniu, sprawdź sam!"
        message += f"\n\nPost: {post.message}"
        message += f"\nNa całe: {game_data.isFullField}"
        message += f"\nData: {game_data.gameDate}"
        message += f"\nPoziom: {game_data.level}"

        message += f"\n\nZobacz: {self.args['group_url']}"
        
        email_notifier.send_email(self.args["email"], "Znaleziono potencjalną grę!", message)

    def comment(self, post, game_data):
        logging.info("Game found: " + post.message)

        post.comment(self.args["comment"], self.driver)

        message = "Znaleziono grę!"
        message += f"\n\nPost: {post.message}"
        message += f"\nNa całe: {game_data.isFullField}"
        message += f"\nData: {game_data.gameDate}"
        message += f"\nPoziom: {game_data.level}"
        message += f"\nSkomentowano: {self.args['comment']}"

        message += f"\n\nZobacz: {self.args['group_url']}"

        email_notifier.send_email(self.args["email"], "Znaleziono grę!", message)

        webbrowser.open_new_tab(self.args['group_url'])
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)

        ctypes.windll.user32.MessageBoxW(0, message, "Znaleziono grę!", 0x1000)