estimulos = input("Responde a Estimulos?: ").upper()

if estimulos == "SI":
  print("Valorar la necesidad de llevarlo al Hospital mas cercano")
else:
  print("Deberar abrir la via Aerea")

respira = input("Respira?: ")
if respira == "SI":
  print("Permite posicion de suficiente Ventilacion")
else:
  print("Administrar 5 Ventilaciones y Llamar a Ambulacia")


ambulancia = "NO"
while ambulancia == "NO":
  signo_vida = input("Tiene signos de vida?: ")
  if signo_vida == "SI":
    print("Reevaluar a la espera de la ambulacia")
  else:
    print("Administrar Compresiones Toracicas hasa que llegue ambulacia")
  ambulancia = input("Llego la ambulancia?: ")
print("Programa Terminado")
