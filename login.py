#!/usr/bin/env python3
import os
import cgi
from secret import real_username, real_password
from templates import after_login_incorrect 

form = cgi.FieldStorage()
username = form['username'].value
password = form['password'].value

if (username == real_username and password == real_password):
    print(f"Set-Cookie:username = {username}")
    print(f"Set-Cookie:password = {password}")
    print("Content-Type: text/html\r\n")
else:
    print(after_login_incorrect())
