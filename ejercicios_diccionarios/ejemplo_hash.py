import hashlib

salida = hashlib.sha256(b'El libro de python').hexdigest()
print (salida)