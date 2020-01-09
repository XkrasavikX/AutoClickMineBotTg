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
with open("configs/data.json", "r") as read_file:
    configs = json.load(read_file)

api_id, api_hash = configs["id"], configs["hash"]

proxy_ip, proxy_port, secret = configs["proxy"]["ip"], configs["proxy"]["port"], configs["proxy"]["secret"]
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
    if dlg.title == 'BCH Click Bot':
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
            client.send_message('BCH Click Bot', "/visit")
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
                        'BCH Click Bot',
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
            client.send_message('BCH Click Bot', "/visit")
            time.sleep(6)
            print("Найдено Sorry")

        else:
            messages = client.get_messages(tegmo)
            url_rec = messages[0].reply_markup.rows[0].buttons[0].url
            f = open("url_dir/urls4.txt")
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
                    'apikey': configs["VirusTotal_apiKey"], 'url': url_rec}
                response = requests.post(url, data=params)
                my_file = open('url_dir/urls4.txt')
                my_file.write(url_rec)
                print("Новая запись в файле сделана")
                time.sleep(16)
                n = n + 1
                print("Пройдено циклов: ", n)
