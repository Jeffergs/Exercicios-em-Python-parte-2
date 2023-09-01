# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, 
# meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
# Considerar ano com 365 dias e mês com 30 dias.

anos = int(input("Idade (em anos): ")) # Quantos anos de vida a pessoa tem
meses = int(input("Idade (em meses): ")) # Quantos meses (a partir do último aniversário) a pessoa tem
dias = int(input("Idade (em dias): ")) # Quantos dias (a partir do último aniversário) a pessoa tem

dias_vividos = (anos * 365) + (meses * 30)# + dias

print(f"Você está vivo a {dias_vividos} dias ")

