import requests
url="https://prod-18.centralindia.logic.azure.com/workflows/d1dfef5cd2b54103b67a989eab024704/triggers/request/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Frequest%2Frun&sv=1.0&sig=ZRSj02or46cAlXseGsDU4VGUd6KqqXqe_U4R_W9Dxhw"
headers={"Name":"Jay Paliwal", "Email":"jay.paliwal2017@vitstudent.ac.in", "College":"Vellore Institute of Technology, Vellore", "StudentId":"17BIT0238", "FileName":"decode.py"}
f=open("/home/jay_paliwal/Desktop/decode.py","r")
file=f.read()
response = requests.put(url, headers=headers, data={"file":file})
print(response.text)
