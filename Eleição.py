# 1°-Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos.
# 2°-Calcule e escrever o percentual que cada um representa em relação ao total de eleitores.


total_eleitores = int(input("Total de eleitores: "))

votos_brancos = int(input("Total de votos brancos: "))
votos_nulos = int(input("Total de votos nulos: "))
votos_validos = int(input("Total de votos válidos: "))

brancos = (votos_brancos * 100) / total_eleitores
nulos = (votos_nulos * 100) / total_eleitores
validos = (votos_validos * 100) / total_eleitores

print(f"Os votos brancos representam {brancos:.2f}% do total de votos computados ")
print(f"Os votos nulos representam {nulos:.2f}% do total de votos computados ")
print(f"Os votos válidos representam {validos:.2f}% do total de votos computados ")