"""
This code should send a request to the url and displays the variable
X-Request-Id in the response header(whatever that is) 
"""

import requests
import sys

#get the url as an input
url = sys.argv[1]

response = requests.get(url)

if response.status_code== 200:
    
    request_id = response.headers.get("X-Request-Id")
    
    
    print (request_id)
    
else:
    print ("failed to do the task. Status code: {request.status_code}")
