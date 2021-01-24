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

---

### Telegram Objects
Telegram Objects in telegrapy are object-oriented implementation of [JSON-objects](https://core.telegram.org/bots/api#available-types) in the Telegram API. They all have a unique identifier and their corresponding JSON. Hence, any object can return its own JSON format by calling the `.json` attribute.

#### User

#### Chat

#### Message

---

### Creating Bot Commands
