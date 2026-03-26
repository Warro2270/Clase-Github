import random

print("Hola, bienvenido al juego de ´piedra, papel, tijeras, lagarto o Spock´")
print("Elige entre estas opciones colocando su numero: \n1: Spock \n2: tijeras \n3: papel \n4: roca \n5: lagarto")
usuario = int(input())
rival = random.randint(1,5)
spock = 1
tijeras = 2
papel = 3
roca = 4
lagarto = 5

resultado = "Empate"

if usuario == 1: #spock
    usuario = "Spock"
    if rival == 2 or rival == 4:
        resultado = "Ganaste"
    elif rival == 3 or rival == 5:
        resultado = "Perdiste"
if usuario == 2: #tijeras
    usuario = "tijeras"
    if rival == 3 or rival == 5:
        resultado = "Ganaste"
    elif rival == 1 or rival == 4:
        resultado = "Perdiste"
if usuario == 3: #papel
    usuario = "papel"
    if rival == 4 or rival == 1:
        resultado = "Ganaste"
    elif rival == 2 or rival == 5:
        resultado = "Perdiste"
if usuario == 4: #roca
    usuario = ""
    if rival == 5 or rival == 2:
        resultado = "Ganaste"
    elif rival == 1 or rival == 3:
        resultado = "Perdiste"
if usuario == 5: #lagarto
    usuario = ""
    if rival == 1 or rival == 3:
        resultado = "Ganaste"
    elif rival == 2 or rival == 4:
        resultado ="Perdiste"

if rival == 1:
    rival = "Spock"
elif rival == 2:
    rival = "tijeras"
elif rival == 3:
    rival = "papel"
elif rival == 4:
    rival = "roca"
elif rival == 5:
    rival = "lagarto"


print("Tu elegiste "+str(usuario)+" y tu rival eligió "+rival)
print(resultado)
