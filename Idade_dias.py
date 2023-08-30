# Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias.
# Considerar ano com 365 dias e mês com 30 dias.

anos = int(input("Idade (anos): ")) # Quantos anos de vida a pessoa tem
meses = int(input("Idade (meses): ")) # Quantos meses (a partir do último aniversário) a pessoa tem
dias = int(input("Idade (dias): ")) # Quantos dias (a partir do último aniversário) a pessoa tem

a = anos * 365 # anos * 365 dias
b = meses * 30 # meses * 30 dias
dias_vividos = a + b + dias

print(f"Você está vivo a {dias_vividos} dias ")

