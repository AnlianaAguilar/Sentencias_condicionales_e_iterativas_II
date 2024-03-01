import getpass
import string

password = getpass.getpass("Ingrese su contraseña: ").lower()

counter = 0


for i in password:
  for j in string.ascii_lowercase:
    if i == j:
      counter += 1
      break
    else:
      counter += 1
print(counter)

