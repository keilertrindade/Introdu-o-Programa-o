# -*- coding: utf-8 -*-
for andar in range (20, 0, -1):
  if andar != 13:
    print(andar)
    
    
andar = 20
while andar > 0:
  if andar != 13:
    print(andar)
  andar -= 1

-------------------------------
"""Faça um código que execute a contagem regressiva de uma bomba, informando o número de segundos para explodir.
Ele deverá mostrar a mensagem “iniciando contagem regressiva”, os segundos passados e, no final, a mensagem “BUM!”.
Não é necessário, mas, caso deseje tornar o sistema mais realista para que o tempo realmente passe em segundos, você pode usar a função time.sleep() que existe na Python (acesse o link em anexo). 
No entanto, é preciso adicionar uma biblioteca antes de executá-la."""

import time
segundos = int(input("Digite a quantidade de segundos: "))
print("Iniciando contagem regressiva!")
for s in range(segundos,0,-1):
  print(f"{s}!")
  time.sleep(1)
print(f"\nBUM!")
