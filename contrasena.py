import random 
caracteres="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
extension= int(input("Escribe la cantidad de caracteres que quieres en tu contraseña  "))
contrasena= ""
for i in range(extension):
    contrasena += random.choice(caracteres)
print(contrasena)
