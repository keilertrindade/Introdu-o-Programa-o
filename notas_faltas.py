"""Desenvolva um programa que utiliza o nome de um aluno, duas notas e a quantidade de faltas que ele teve. Conclua se o aluno está aprovado ou reprovado de acordo com as especificações:

- Se a média do aluno for menor que sete, o sistema deve informar o nome do aluno e que ele está reprovado;
- Se o aluno possuir mais de três faltas, o sistema deve informar o nome do aluno e que ele está reprovado; 
- Se a média do aluno for maior ou igual a sete, o sistema deve informar o nome do aluno e que ele está aprovado. 

No sistema, todos os valores devem estar armazenados em variáveis."""


nome_aluno = input("Nome do aluno: ")
faltas = int(input("Quantidade de faltas: "))
nota_1 = float(input("Digite a nota 01: "))
nota_2 = float(input("Digite a nota 02: "))
media = (nota_1 + nota_2)/2

if (media < 7):
  print(f"Aluno {nome_aluno} reprovado com nota {media}")
elif (faltas > 3):
  print(f"Aluno {nome_aluno} reprovado por faltas!")
else:
  print(f"Aluno {nome_aluno} aprovado com nota {media}")
