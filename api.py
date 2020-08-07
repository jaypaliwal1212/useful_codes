"this is a code which allows a user to upload a file by consuming an api through put request method"

import requests
url="https://url"
headers={"Name":"Jay Paliwal", "key2":"value2"}
f=open("/path/filetobeuploaded.extention","r")
file=f.read()
response = requests.put(url, headers=headers, data={"file":file})
print(response.text)
