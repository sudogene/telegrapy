from telegrapy import Bot, Message
import time

# Obtain token and create bot. See https://core.telegram.org/bots#6-botfather
token = 'YOUR_TOKEN_HERE'
bot = Bot(token)

# Get handler of bot, for adding of handler functions
handler = bot.handler


# All handler functions takes in one argument: Message
def echo(msg: Message):
    chat_id = msg.chat_id
    text = msg.text
    bot.send_message(chat_id, text)


# Add defined handler function to the bot with specified command word
# users can call this function by sending "/echo sample text" to the bot
handler.add_command('echo', echo)


def main():
    bot.run()
    print('Running...')
    while True:
        time.sleep(3)


main()
