import game_data_retriever
from datetime import datetime, timedelta
from game_action import *

def get_action(game_data, args):
    if not game_data.isGameOffer:
        return IGNORE

    if not game_data.isOnAGH:
        return IGNORE

    if game_data.gameDate < args["start_date"]:
        return IGNORE
    
    if game_data.gameDate > args["end_date"]:
        return IGNORE

    if args["level"] and game_data.level != args["level"]:
        return NOTIFY

    if args["full_field_only"] and not game_data.isFullField:
        return NOTIFY

    if game_data.gameDate < datetime.now() + timedelta(minutes=args["advance_min"]):
        return NOTIFY

    return COMMENT