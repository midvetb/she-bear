def add_to_blacklist(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        client.block_user(user_id)
    else:
        pass


def remove_from_blacklist(client, message):
    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        client.unblock_user(user_id)
    else:
        pass
