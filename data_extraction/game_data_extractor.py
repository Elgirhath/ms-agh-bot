from post_gatherer import Post
from data_extraction import game_date_extractor
from data_extraction import game_location_extractor
from data_extraction import full_field_extractor
from data_extraction import level_extractor
from data_extraction import game_offer_extractor

class GameData:
    def __init__(self, isGameOffer, gameDate, isOnAGH, isFullField, level):
        self.isGameOffer = isGameOffer
        self.gameDate = gameDate
        self.isOnAGH = isOnAGH
        self.isFullField = isFullField
        self.level = level

def extract_game_data(post : Post):
    gameDate = game_date_extractor.extract_game_date(post)
    isOnAGH = game_location_extractor.extract_is_on_agh(post)
    isFullField = full_field_extractor.extract_is_full_field(post)
    level = level_extractor.extract_level(post)
    isGameOffer = game_offer_extractor.extract_is_game_offer(post)
    if gameDate is None:
        isGameOffer = False

    return GameData(isGameOffer, gameDate, isOnAGH, isFullField, level)