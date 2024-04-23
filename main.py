from pyrogram import Client, filters
from handlers import message_handlers
import subprocess as sp
from dotenv import load_dotenv
import os


load_dotenv()


api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")


app = Client("she-bear", api_id, api_hash)
msg_handler = message_handlers


with app:
    get_me = app.get_me()
    my_id = get_me.id


def is_me(_, __, message):
    return message.from_user and message.from_user.id == my_id


@app.on_message(filters.command("exec"))
def evaluate_command(client, message):
    if message.from_user.id != my_id:
        return


    command = message.text[len("/exec"):].strip()


    try:
        if command.startswith("python"):
            command = command.replace("python", "", 1).lstrip()
            result = sp.run(["python3", "-c", command], capture_output=True, text=True)


            if result.returncode == 0:
                client.send_message(message.chat.id, result.stdout)
            else:
                client.send_message(message.chat.id, f"ашыпк выполнен: {result.stderr}")
        else:
            result = sp.run(command, shell=True, capture_output=True, text=True)


            if result.returncode == 0:
                client.send_message(message.chat.id, result.stdout)
            else:
                client.send_message(message.chat.id, f"ашыпк выполнен: {result.stderr}")
    except Exception as err:
        client.send_message(message.chat.id, f"ашыпк: {err}")


@app.on_message(filters.create(is_me))
def handler_message(client, message):
    msg_handler.handle_message(client, message)


app.run()