#!/usr/bin/env python3
import lxml.html as html
import cgi
import requests
import json
form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")
text2 = str(text1)
default = "none"
r = requests.get('https://public-api.nazk.gov.ua/v1/declaration/'+text2)
parsed_json = json.loads(r.text)
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print (parsed_json.get("data")['step_3']['1477321890754']['objectType'])

print("""</body>
        </html>""")
