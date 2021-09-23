#!/usr/bin/env python3
import os
import json
from templates import login_page, secret_page

print("Content-type:text/html\r\n")
diction = dict(os.environ)

if len(diction["HTTP_COOKIE"]) > 1:
    cookies = diction["HTTP_COOKIE"].split(";")
    username = cookies[0][cookies[0].find('=')+1:]
    password = cookies[1][cookies[1].find('=')+1:]
    print(secret_page(username, password))
else:
    print(login_page())
