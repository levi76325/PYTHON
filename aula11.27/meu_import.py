preco = float(input("informe o preço do seu produto: "))

desconto1 = 0.2
desconto2 = 0.5
desconto3 = 0.8

valor = preco * desconto2
if preco < 100:
    valor = preco * desconto1
elif preco >= 100 and preco <= 500:
    valor = preco * desconto2
elif preco > 500:
    valor = preco * desconto3
else:
    print(f'o preço { preco } não tem desconto.')