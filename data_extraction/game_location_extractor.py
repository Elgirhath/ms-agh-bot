from post_gatherer import Post

field_blacklist = [
    "dekerta",
    "tynieck",
    "bronowiank"
]

field_whitelist = [
    "miasteczko",
    "agh",
    "piastowsk"
]

def extract_is_on_agh(post : Post):
    message = post.get_normalized_message()

    for field in field_blacklist:
        if field in message:
            return False

    if "hala" in message or "hali" in message:
        return False

    for field in field_whitelist:
        if field in message:
            return True

    if "ul." in message:
        return False

    return True