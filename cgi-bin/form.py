#!/usr/bin/env python3
import lxml.html as html
import cgi
import requests
import json
form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1")
text2 = str(text1)
default = "none"
r = requests.get('https://public-api.nazk.gov.ua/v1/declaration/?q='+text2)
parsed_json = json.loads(r.text)
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")
num_ell = (parsed_json.get("page")["totalItems"])
#print (parsed_json.get("items")[2]["id"])
ids = 0
idss = []
while ids < num_ell:
	idss[] = (parsed_json.get("items")[ids]["id"])
	ids=ids+1
	print ("<a href https://public-api.nazk.gov.ua/v1/declaration/"+idss[])+"></a>"

print("""</body>	
        </html>""")

