from pyfiglet import Figlet
from colorama import Fore, Style
import os
import urllib.request as urllib2
import json

while True:
    text_preview = Figlet(font='slant')
    print(Fore.RED + text_preview.renderText('IP CHECKER') + Style.RESET_ALL)

    ip = input(Fore.GREEN + "What is your target IP: " + Style.RESET_ALL)
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url + ip)
    data = response.read()
    values = json.loads(data)
    print(Fore.GREEN + f"IP: {values['query']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"City: {values['city']}" + Style.RESET_ALL + Style.RESET_ALL)
    print(Fore.GREEN + f"ISP: {values['isp']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Country: {values['country']}" + Style.RESET_ALL)
    print(Fore.GREEN + f"Region: {values['region']}")
    print(Fore.GREEN + f"Timezone: {values['timezone']}" + Style.RESET_ALL)
    continue_num = int(input("Введите 1 если хотите пробить ещё ра, 2 если завершить"))
    if continue_num == 2:
        break


  # print(Fore.RED + "Красный текст" + Style.RESET_ALL)
  # print(Fore.GREEN + "Зеленый текст" + Style.RESET_ALL)


