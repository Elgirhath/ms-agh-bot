import re
import datetime
from datetime import timedelta
from post_gatherer import Post

weekday_list = [
    'poniedzialek',
    'wtorek',
    'sroda',
    'czwartek',
    'piatek',
    'sobota',
    'niedziela'
]

def extract_time(message):
    time_matches = re.search("(\d?\d)[:.](\d[05])", message)
    if time_matches:
        time = (int(time_matches.groups()[0]), int(time_matches.groups()[1]))
        if validate_time(*time):
            return time
        
    time_matches = re.search("o (\d?\d)", message)
    if time_matches:
        time = (int(time_matches.groups()[0]), 0)
        if validate_time(*time):
            return time
        
    time_matches = re.search("na (\d?\d)", message)
    if time_matches:
        time = (int(time_matches.groups()[0]), 0)
        if validate_time(*time):
            return time
        
    time_matches = re.search("(\d?\d)-\d", message)
    if time_matches:
        time = (int(time_matches.groups()[0]), 0)
        if validate_time(*time):
            return time
        
    time_matches = re.search("dzisiaj (\d?\d)", message)
    if time_matches:
        time = (int(time_matches.groups()[0]), 0)
        if validate_time(*time):
            return time
        
    time_matches = re.search("dzis (\d?\d)", message)
    if time_matches:
        time = (int(time_matches.groups()[0]), 0)
        if validate_time(*time):
            return time

    if "teraz" in message:
        time = datetime.datetime.now().timetuple()
        return (time.tm_hour, time.tm_min)

    return None

def validate_time(hours, mins):
    if hours > 23 or hours < 0:
        return False
    if mins > 59 or mins < 0:
        return False
    return True

def extract_game_date(post : Post):
    message = post.get_normalized_message()

    posttime = None
    if "godz." in post.time:
        hourdiff = -int(post.time[:2])
        posttime = datetime.datetime.now() + timedelta(hours=hourdiff)
    elif "dni" in post.time:
        daydiff = -int(post.time[:2])
        posttime = datetime.datetime.now() + timedelta(days=daydiff)
    else:
        posttime = datetime.datetime.now()
        
    posttime_day_of_year = posttime.timetuple().tm_yday
    posttime_day_of_week = posttime.timetuple().tm_wday

    day_offset = 0
    if "jutro" in message:
        day_offset = 1
    elif "pojutrze" in message:
        day_offset = 2

    for idx, weekday in enumerate(weekday_list):
        if weekday in message:
            day_offset = (idx - posttime_day_of_week) % 7

    game_datetime = posttime + timedelta(days=day_offset)

    time = extract_time(message)

    if time is None:
        return None

    return game_datetime.replace(hour=time[0], minute=time[1], second=0)
