import hashlib

text = 'Hello'
textencode = text.encode()
md5 = hashlib.md5(textencode)
print(textencode,md5)
#md5.update(text)
#print(md5.hexdigest())