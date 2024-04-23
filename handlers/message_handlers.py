from commands import blacklist


def handle_message(client, message):
    if isinstance(message.text, str):

        if message.text.lower() == "чс":
            blacklist.add_to_blacklist(client, message)
        elif message.text.lower() == "нечс":
            blacklist.remove_from_blacklist(client, message)
        else:
            pass
    else:
        pass
