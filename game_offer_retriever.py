from post_gatherer import Post


def retrieve_is_game_offer(post : Post):
    message = post.get_normalized_message()
    
    if "szukam gierki" in message:
        return False

    if "zagram " in message:
        return False

    return True