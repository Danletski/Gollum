import requests 

#Check nginx is up
nginx = 'http://localhost:85' 
response = requests.get(nginx)        # To execute get request 
if response.status_code == 200:
    print('Success!')
elif response.status_code != 200:
    print('Not Found.')

#Check Web_app1 is up
web1 = 'http://localhost:8081' 
response = requests.get(web1)        # To execute get request 
if response.status_code == 200:
    print('Success!')
elif response.status_code != 200:
    print('Not Found.')

#Check Web_app2 is up
web2 = 'http://localhost:8082' 
response = requests.get(web2)
if response.status_code == 200:
    print('Success!')
elif response.status_code != 200:
    print('Not Found.')
