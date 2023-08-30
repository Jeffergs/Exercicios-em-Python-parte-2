# Dada a quilometragem parcial de um carro e a quantidade de litros gastos ele para percorrer esta quilometragem, faça um algoritmo que calcule quantos Km/l o carro percorreu.

km = float(input("Kms percorridos: "))
litro_gasolina = float(input("Quantidade de litros utilizada: "))

kml = km / litro_gasolina

if(kml <= 1):
  print(f"O carro percorreu {kml:.1f} quilometro por litro")

else:
  print(f"O carro percorreu {kml:.1f} quilometros por litro")