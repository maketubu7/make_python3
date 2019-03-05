import requests
import re

html = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={0}'
nothing = '12345'

regex = '[0-9]+'

response = requests.get(html.format(nothing))
while response.status_code == 200:
    response = requests.get(html.format(nothing))
    text = response.text
    nothing = ''.join(re.findall(regex, text))
    print(text)

