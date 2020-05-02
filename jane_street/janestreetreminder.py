import requests
import time as time
import telegram
from bs4 import BeautifulSoup
my_token = "//insert your token // look for BotFather on Telegram>>Create New Bot"
ids = ["000"]
URL = "https://www.janestreet.com/puzzles/current-puzzle/"

def send(msg, chats=ids, token=my_token):
    bot = telegram.Bot(token=token)
    for chat in ids:
        bot.sendMessage(chat_id=chat, text=msg)


page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

oldtitle = soup.find(class_ = 'puzzle-post-title').text
title = oldtitle
print(title)

send("Bot S8plus avviato")
while title == oldtitle: 
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(class_ = "puzzle-post-title").text
    time.sleep(5)

if title != oldtitle:
    send("Disponibile nuovo puzzle sul sito di Jane Street, vedi:\n\n https://www.janestreet.com/puzzles/current-puzzle/")
else: 
    send("Bot spento per qualche motivo sconosciuto all'abile programmatore")


