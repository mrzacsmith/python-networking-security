import requests
import re

# data variable to get URL
data = requests.get('https://www.yellowpages.com.au/find/speech-pathologists/perth-wa-6000')

# general regex to extract
phones = re.findall(r'(\(?[0-9]{3}\)?(?:\-|\s|\.)?[0-9]{3}(?:\-|\.)[0-9]{4})', data.text)
emails = re.findall(r'([\d\w\.]+@[\d\w\.\-]+\.\w+)', data.text)

print(phones, emails)