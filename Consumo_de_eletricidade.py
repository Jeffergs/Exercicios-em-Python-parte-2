#  Crie um algoritmo que solicite ao usuário seu consumo de energia elétrica (em kWh), que deve ser uma variável real.
#  O algoritmo deve, então, calcular o total da conta, considerando que cada kWh custa R$ 0,20.


kwh = 0.2 # --> Valor de 1 KWh
quantidade_kwv = float(input("KWh consumidos neste mês: "))

resultado = quantidade_kwv * kwh

# Valor do consumo de energia:
print(f"Seu consumo de energia foi de {resultado:.2f} neste mês")