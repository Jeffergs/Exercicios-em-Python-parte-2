# Tendo como base o valor da cotação do dólar (em reais) do dia, faça a conversão de um valor em dólares para reais

real = 4.87  #Cotação do dolar em real no dia 29/08/23

dolar = float(input("Quantos dolares você tem: "))

total = dolar * real

print(f"Você tem {total:.2f} reais")
