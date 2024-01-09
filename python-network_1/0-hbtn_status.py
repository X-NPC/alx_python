"""
the following code should fetch(get) the url https://alu-intranet.hbtn.io/status
and state some informaitons

"""

import requests

url = "https://alu-intranet.hbtn.io/status"

response = requests.get(url)

print ("Body response:")
print (f"\t- type: {type(response.text)}")
print (f"\t- content: {response.text}")