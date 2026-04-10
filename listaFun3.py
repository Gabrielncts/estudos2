qtdPao = int(input("Digite a quantidade de pães franceses vendidos: "))
qtdBroa = int(input("Digite a quantidade de broas vendidas: "))
valorPao = 0.12
valorBroa = 1.50
total = (qtdPao * valorPao) + (qtdBroa * valorBroa)
guardar = total * 0.10
print(f"Faturamento total: R${total: .2f}")
print(f"Valor para guardar: R${guardar: .2f}")