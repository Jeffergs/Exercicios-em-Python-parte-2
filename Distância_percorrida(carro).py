# Dada a quilometragem parcial de um carro e a quantidade de litros gastos ele para percorrer esta quilometragem, faça um algoritmo que calcule quantos Km/l o carro percorreu.

kms_percorridos = float(input("Kms percorridos: "))
litro_gasolina = float(input("Quantidade de litros utilizada: "))

kmlitros = kms_percorridos / litro_gasolina

if(kmlitros <= 1):
  print(f"O carro percorreu {kmlitros:.1f} quilometro por litro")

else:
  print(f"O carro percorreu {kmlitros:.1f} quilometros por litro")
