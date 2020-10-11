#!/usr/bin/env python3

import requests

with requests.Session() as s:
    for i in range(1, 40):
        r = s.get("http://15.206.202.26/cookie.php")
        print(s.cookies.get("Our_Fav_Cookie"))