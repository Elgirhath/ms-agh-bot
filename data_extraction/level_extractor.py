from post_gatherer import Post

low_whitelist = [
    "reakreac",
    "niski",
    "amator"
]

middle_whitelist = [
    "sredni"
]

high_whitelist = [
    "dobry"
]

veryhigh_whitelist = [
    "dobry+"
    "dobry +"
]

def extract_level(post : Post):
    message = post.get_normalized_message()
    
    for item in low_whitelist:
        if item in message:
            return "rekreacyjny"

    for item in middle_whitelist:
        if item in message:
            return "sredni"
            
    for item in veryhigh_whitelist:
        if item in message:
            return "pro"
            
    for item in high_whitelist:
        if item in message:
            return "dobry"

    return "rekreacyjny"