from post_gatherer import Post

def extract_is_full_field(post : Post):
    message = post.get_normalized_message()

    if "polow" in message:
        return False

    if "cale" in message:
        return True
    
    if "czesc" in message:
        return False

    return True