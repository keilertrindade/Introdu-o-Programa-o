"""
Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
1. Soma
2. Subtração
3. Multiplicação
4. Divisão

Caso seja inserido um número de operação que não exista, o resultado deverá ser 0."""

def calculadora(valor_1, valor_2, operacao):
  if operacao == 1:
    return valor_1 + valor_2
  elif operacao == 2:
    return valor_1 - valor_2
  elif operacao == 3:
    return valor_1 * valor_2
  elif operacao == 4:
   return valor_1 / valor_2
  else:
    return 0

valor_1 = float(input("Digite o primeiro valor: "))
valor_2 = float(input("Digite o segundo valor: "))
operacao = int(input(f"\nSelecione a operação: \n1. Soma\n2. Subtração\n3. Multiplicação\n4. Divisão\n"))
print("Resultado: ",calculadora(valor_1,valor_2,operacao))
