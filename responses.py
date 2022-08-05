import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'troll':
        return 'Minor amounts of trolling'

    if p_message == 'roll':
        return str(random.randInt(1, 20))

    if p_message == 'cringe':
        return '@1nvictus is cringe'
