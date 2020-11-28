from post_gatherer import Post
import game_date_retriever
import game_location_retriever
import full_field_retriever
import level_retriever
import game_offer_retriever

class GameData:
    def __init__(self, isGameOffer, gameDate, isOnAGH, isFullField, level):
        self.isGameOffer = isGameOffer
        self.gameDate = gameDate
        self.isOnAGH = isOnAGH
        self.isFullField = isFullField
        self.level = level

def retrieve_game_data(post : Post):
    gameDate = game_date_retriever.retrieve_game_date(post)
    isOnAGH = game_location_retriever.retrieve_is_on_agh(post)
    isFullField = full_field_retriever.retrieve_is_full_field(post)
    level = level_retriever.retrieve_level(post)
    isGameOffer = game_offer_retriever.retrieve_is_game_offer(post)
    if gameDate is None:
        isGameOffer = False

    return GameData(isGameOffer, gameDate, isOnAGH, isFullField, level)