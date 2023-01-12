import requests

print(requests.__version__)

print(requests.get('https://www.google.com/'))

r = requests.get("https://raw.githubusercontent.com/adhanani90/cmput_404_lab1/master/script.py")
print(r.text)