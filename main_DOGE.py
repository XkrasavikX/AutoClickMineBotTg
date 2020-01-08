from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telethon import sync, events
import requests
import json
import hashlib
import time
import re
from virus_total_apis import PublicApi as VirusTotalPublicApi
from telethon import TelegramClient, connection
import webbrowser
import urllib.request
import os

n = 0

api_id = 1085894
api_hash = '232b522f4fb6843d0a0245dff1b0d993'

proxy_ip = 'russia.proxy.digitalresistance.dog'
proxy_port = 443
secret = 'ddd41d8cd98f00b204e9800998ecf8427e'
# client = TelegramClient('anon1', api_id, api_hash)
# client.connect()
client = TelegramClient(
    'anon',
    api_id,
    api_hash,
    connection=connection.ConnectionTcpMTProxyRandomizedIntermediate,
    proxy=(proxy_ip, proxy_port, secret)
)
client.start()

dlgs = client.get_dialogs()

for dlg in dlgs:
    if dlg.title == 'DOGE Click Bot':
        tegmo = dlg
print(tegmo)


class RunChromeTests():
    def testMethod(self):
        caps = {'browserName': 'chrome'}
        driver = webdriver.Remote(command_executor=f'http://localhost:4444/wd/hub', desired_capabilities=caps)
        driver.maximize_window()
        driver.get(url_rec)
        time.sleep(waitin + 10)
        driver.close()
        driver.quit()


print('start')
while True:
    msgs = client.get_messages(tegmo, limit=1)
    for mes in msgs:
        if re.search(r'\bseconds to get your reward\b', mes.message):
            print("Найдено reward")
            str_a = str(mes.message)
            zz = str_a.replace('You must stay on the site for', '')
            qq = zz.replace('seconds to get your reward.', '')
            waitin = int(qq)
            print("Ждать придется: ", waitin)
            client.send_message('DOGE Click Bot', "/visit")
            time.sleep(3)
            msgs2 = client.get_messages(tegmo, limit=1)
            for mes2 in msgs2:
                button_data = mes2.reply_markup.rows[1].buttons[1].data
                message_id = mes2.id

                print("Перехожу по ссылке")
                time.sleep(2)
                url_rec = messages[0].reply_markup.rows[0].buttons[0].url
                ch = RunChromeTests()
                ch.testMethod()
                time.sleep(6)
                fp = urllib.request.urlopen(url_rec)
                mybytes = fp.read()
                mystr = mybytes.decode("utf8")
                fp.close()
                if re.search(r'\bSwitch to reCAPTCHA\b', mystr):
                    from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

                    resp = client(GetBotCallbackAnswerRequest(
                        'DOGE Click Bot',
                        message_id,
                        data=button_data
                    ))
                    time.sleep(2)
                    print("КАПЧА!")
                    # os.system("pkill chromium")
                else:
                    time.sleep(waitin)
                    # os.system("pkill chromium")
                    time.sleep(2)

        elif re.search(r'\bSorry\b', mes.message):
            client.send_message('DOGE Click Bot', "/visit")
            time.sleep(6)
            print("Найдено Sorry")

        else:
            messages = client.get_messages(tegmo)
            url_rec = messages[0].reply_markup.rows[0].buttons[0].url
            f = open("url_dir/urls3.txt")
            fd = f.read()
            if fd == url_rec:
                print("Найдено повторение переменной")
                msgs2 = client.get_messages(tegmo, limit=1)
                for mes2 in msgs2:
                    button_data = mes2.reply_markup.rows[1].buttons[1].data
                    message_id = mes2.id
                    from telethon.tl.functions.messages import GetBotCallbackAnswerRequest

                    resp = client(GetBotCallbackAnswerRequest(
                        tegmo,
                        message_id,
                        data=button_data
                    ))
                    time.sleep(2)
            else:
                url = 'https://www.virustotal.com/vtapi/v2/url/scan'
                params = {
                    'apikey': '5e690fc1a04f6c08c6d008ba39606cf30244df0b0621597c6ef67548fc9c85a1', 'url': url_rec}
                response = requests.post(url, data=params)
                my_file = open('url_dir/urls3.txt')
                my_file.write(url_rec)
                print("Новая запись в файле сделана")
                time.sleep(16)
                n = n + 1
                print("Пройдено циклов: ", n)
