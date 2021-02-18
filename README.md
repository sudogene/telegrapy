# Telegrapy

Telegrapy is a package for easy building of bots using the [Telegram Bot API](https://core.telegram.org/bots). 

---

### How to start
1. Clone the repo
```
$ cd PATH_OF_YOUR_CHOICE
$ git clone https://github.com/sudogene/telegrapy.git
$ cd telegrapy
```
OR install package
```
$ pip3 install telegrapy
```

2. Test your bot's account using the following code
```
from telegrapy import Bot

token = 'YOUR_TOKEN'
bot = Bot(token)

print(bot.get_me())
```

3. Set bot to run in a loop and keep program alive
```
bot.run()
print('Running...')

while True:
  time.sleep(3)
```
When the bot runs, it indefinitely checks for message updates and handles them.

Quick example on an echo bot can be found in [example.py](example.py).

---

### Telegram Objects
Telegram Objects in telegrapy are object-oriented implementation of [JSON-objects](https://core.telegram.org/bots/api#available-types) in the Telegram API. Each object has a unique identifier (ID) and its corresponding JSON. Hence, any object can return its own JSON format by calling the `.json` attribute.

#### User
Based on Telegram [User](https://core.telegram.org/bots/api#user). These are typically senders of `Message`.

#### Chat
Based on Telegram [Chat](https://core.telegram.org/bots/api#chat). They are subclassed into `PrivateChat`, `GroupChat`, and `SupergroupChat`. As of now, there are not many differences in terms of parsing messages from these chat types. Chat IDs are required for bots to send messages to.

#### Message
Based on Telegram [Message](https://core.telegram.org/bots/api#message). The main bulk of data necessary for bot interactions. Contains information of the date time, sender, chat, command, and text.

---

### Creating Bot Commands
Bot commands are special text/phrases recognized by bots as commands, and trigger bots to call functions defined by the user. All messages received by the bot are parsed and handled by the `Handler` class which is attached to the Bot upon creation. You can create your handler functions using the function signature 
```
def function_name(msg: telegrapy.Message)
```
where all functions MUST take in the `Message` object. A code example:
```
def echo(msg):
  chat_id = msg.chat_id
  text = msg.text
  bot.send_message(chat_id, text)
```
Defined handler functions can then be added to the bot's handler:
```
# get the handelr
handler = bot.handler

# add the function
handler.add_command('echo', echo)
```
Adding of commands to the handler requires two arguments; the string command and the function.

---

### Bot Methods
Not to be confused with bot commands. Bot methods are GET and POST HTTP methods based on Telegram [Available Methods](https://core.telegram.org/bots/api#available-methods). As of now, the following methods have been implemented in this library:

Method | telegrapy.Bot function
-------- | --------
[getMe](https://core.telegram.org/bots/api#getme) | `get_me`
[sendMessage](https://core.telegram.org/bots/api#sendmessage) | `send_message`
[sendPhoto](https://core.telegram.org/bots/api#sendphoto) | `send_photo`
[sendAudio](https://core.telegram.org/bots/api#sendaudio) | `send_audio`
[sendDocument](https://core.telegram.org/bots/api#senddocument) | `send_document`
[sendVideo](https://core.telegram.org/bots/api#sendvideo) | `send_video`
[sendVoice](https://core.telegram.org/bots/api#sendvoice) | `send_voice`
[sendDice](https://core.telegram.org/bots/api#senddice) | `send_dice`

#### Optional Arguments for Bot Methods
Some methods support additional arguments specific to use case. An example is `reply_to_message_id` which allows the bot's message to reply to a specific message. This requires the Message ID, which is conveniently available in the `Message` input for all handler functions.
```
# Direct reply to the sender's message
def echo(msg):
  chat_id = msg.chat_id
  text = msg.text
  bot.send_message(chat_id, text, reply_to_message_id=msg.id)

bot.handler.add_command('echo', echo)
```

... More to be added
