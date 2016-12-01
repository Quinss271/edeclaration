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
            
            <title>Обработка данных форм</title>
        </head>
        <body>""")
num_ell = (parsed_json.get("page")["totalItems"])
#print (parsed_json.get("items")[2]["id"])

	
print ("""<form action="form2.py">""")
ids = -1
idss = []
while ids < num_ell:
	
	idss = (parsed_json.get("items")[ids]["id"])
	names = (parsed_json.get("items")[ids]["firstname"])
	familys = (parsed_json.get("items")[ids]["lastname"])
	print("<input type='radio' name='petuch' value="+idss+"> "+names, familys+"<Br>")
	ids=ids+1 
print("""<input type='submit'>
	</form>
	""")
    

	
	

print("""</body>	
        </html>""")
