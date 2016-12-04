#!/usr/bin/env python3
import lxml.html as html
import cgi
import requests
import json
form = cgi.FieldStorage()
idss2 = form.getfirst("petuch")
text2 = str(idss2)
default = "none"
r = requests.get('https://public-api.nazk.gov.ua/v1/declaration/'+text2)
parsed_json = json.loads(r.text)


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            
            <title>Обработка данных форм</title>
        </head>
        <body>""")
print("""
	<table>
	<thead>
	<tr><th>Найменування</th>
	<th>Вартість</th>
	</tr>
	</thead>
	<tbody>	""")
ch = -1
hz_kak_nazvat = {}
while ch < 0 :
	idds=  (parsed_json.get("data")["step_3"])
	for key in idds:
		objectTypest3 = (parsed_json.get("data")["step_3"][key]["objectType"])
		print("""<tr><th> Тип об'єкту</th>
		<th>"""+objectTypest3+"""</th>""")
	ch=ch+1
print("""</tr>
</tbody>
</table>

	""")
print("""</body>	
        </html>""")
