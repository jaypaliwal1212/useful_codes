"""This is a simple code which allows user to select a .b64 file, decode it and write the data obtained into a pdf"""


import base64
f = open("/path/Encoded_File.b64","r")
c = open("/path/output_file.pdf","wb") 
text = base64.b64decode(f.read(),validate=True)
f.close()
c.write(text)
c.close()
