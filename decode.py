import base64
f = open("/home/jay_paliwal/Downloads/Encoded_File.b64","r")
c = open("/home/jay_paliwal/Downloads/file.pdf","wb") 
text = base64.b64decode(f.read(),validate=True)
f.close()
c.write(text)
c.close()
