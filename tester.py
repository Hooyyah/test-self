from requests import get
from re import findall
from rubika.client import Bot
import time

bot = Bot("rubika", auth= "nrglmtmgcmahqybmwxojkbvjqqcdkduw")

chnl = "c0BGhaZ0a4becdbff4270923879094b6"
while True:
    try :
        time.sleep(30)
        x = get("https://api.codebazan.ir/bio").text
        cp = f"کانال بیو ما \n @The_Python"
        jok = f"{x}  \n {cp} \n "
        bot.sendMessage(chnl, jok)
        print('sended')
    except :
        print(False)