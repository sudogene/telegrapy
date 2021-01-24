# telegrapy

telegrapy is a package for easy building of Bots using the [Telegram Bot API](https://core.telegram.org/bots). 

---

### How to start (for now)
1. Clone the repo
```
$ cd PATH_OF_YOUR_CHOICE
$ git clone https://github.com/sudogene/telegrapy.git
$ cd telegrapy
```

2. Test your bot's account using the following code
```
import telegrapy

token = 'YOUR_TOKEN'
bot = telegrapy.Bot(token)

print(bot.get_me())
```

3. Set bot to run in a loop and keep program alive
```
bot.run()
print('Running...')

while True:
  time.sleep(3)
```
When the bot runs, it indefinitely checks for message updates and handles them (if any handler function is implemented).

Quick example on an echo bot can be found in [example.py](example.py).

---

### Telegram Objects
Telegram Objects in telegrapy are object-oriented implementation of [JSON-objects](https://core.telegram.org/bots/api#available-types) in the Telegram API. They all have a unique identifier and their corresponding JSON. Hence, any object can return its own JSON format by calling the `.json` attribute.

#### User

#### Chat

#### Message

---

### Creating Bot Commands
All messages received by the bot are parsed and handled by the `Handler` class which is attached to the Bot upon creation. You can create your handler functions using the function signature `def function_name(msg: telegrapy.Message)` where all functions MUST take in the `Message` object. A code example:
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
Adding of commands to the handler requires two arguments; 1. the command string which will trigger the function. 2. the function.

