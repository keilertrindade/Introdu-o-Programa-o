# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVRxhxzjvEp9aUwoS62BDkRETSbCADub
"""

"""Desenvolva um código que utilize as seguintes características de um veículo:
- Quantidade de rodas;
- Peso bruto em quilogramas;
- Quantidade de pessoas no veículo.

Com essas informações, o programa mostrará qual é a melhor categoria de habilitação para o veículo informado a partir das condições:
A: Veículos com duas ou três rodas;
B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;
C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;
D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas; 
E: Veículos com quatro rodas ou mais e com mais de 6000 kg."""


quantidade_rodas = int(input("Quantidade de rodas do veículo: "))
peso_bruto = int(input("Peso bruto(kg): "))
quantidade_pessoas = int(input("Quantidade de pessoas no veículo: "))


if (quantidade_rodas == 3 or quantidade_rodas == 2):
  print(f"Categoria de habilitação A")
elif (quantidade_rodas == 4 and quantidade_pessoas <= 8 and peso_bruto <= 3500):
  print(f"Categoria de habilitação B")
elif (quantidade_rodas >= 4 and peso_bruto > 3500 and peso_bruto <= 6000):
  print(f"Categoria de habilitação C")
elif (quantidade_rodas >= 4 and quantidade_pessoas > 8):
  print(f"Categoria de habilitação D")
elif (quantidade_rodas >= 4 and peso_bruto > 6000):
  print(f"Categoria de habilitação E")