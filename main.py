"""
Faça um programa na linguagem python que receba as seguintes informações de dez pessoas: idade, peso, altura. Calcule e mostre:
a) A media da idade das pessoas;
b) A quantidade de pessoas com peso superior a 90kg e altura inferior a 1,50 metros;
c) A porcentagem de pessoas com idade entre 10 e 30 anos em relação ao numero total de pessoas.
d) Qual a idade da pessoa mais jovem;
e) Qual a altura da pessoa mais alta;
"""
# Inicializa as variáveis para armazenar as informações das pessoas
idades = [0] * 10
pesos = [0.0] * 10
alturas = [0.0] * 10

# Loop para receber as informações de 10 pessoas
for i in range(10):
    print(f"Informações da pessoa {i+1}:")
    idade = int(input("Idade: "))
    peso = float(input("Peso (em kg): "))
    altura = float(input("Altura (em metros): "))
    
    # Armazena as informações nas listas correspondentes
    idades[i] = idade
    pesos[i] = peso
    alturas[i] = altura

# Cálculo da média de idade
soma_idades = 0
for i in range(10):
    soma_idades += idades[i]
media_idade = soma_idades / 10
print(f"Média de idade: {media_idade:.2f}")

# Contagem de pessoas com peso superior a 90kg e altura inferior a 1,50 metros
contagem = 0
for i in range(10):
    if pesos[i] > 90 and alturas[i] < 1.5:
        contagem += 1
print(f"Quantidade de pessoas com peso superior a 90kg e altura inferior a 1,50 metros: {contagem}")

# Cálculo da porcentagem de pessoas com idade entre 10 e 30 anos
contagem = 0
for i in range(10):
    if idades[i] >= 10 and idades[i] <= 30:
        contagem += 1
porcentagem = contagem / 10 * 100
print(f"Porcentagem de pessoas com idade entre 10 e 30 anos: {porcentagem:.2f}%")

# Encontrar a idade da pessoa mais jovem
idade_minima = idades[0]
for i in range(1, 10):
    if idades[i] < idade_minima:
        idade_minima = idades[i]
print(f"Idade da pessoa mais jovem: {idade_minima}")

# Encontrar a altura da pessoa mais alta
altura_maxima = alturas[0]
for i in range(1, 10):
    if alturas[i] > altura_maxima:
        altura_maxima = alturas[i]
print(f"Altura da pessoa mais alta: {altura_maxima:.2f} metros")