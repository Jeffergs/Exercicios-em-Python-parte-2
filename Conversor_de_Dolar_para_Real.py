# Tendo como base o valor da cotação do dólar (em reais) do dia, faça a conversão de um valor em dólares para reais

valor_cotacao = float(input("Digite o valor da cotação do dólar: "))
dolar = float(input("Quantos dolares você tem: "));

total = dolar * valor_cotacao

print(f"Você tem R$ {total:.2f} reais");
print(f"{dolar:.2f} dolares convertido para reais é R$ {total}");
