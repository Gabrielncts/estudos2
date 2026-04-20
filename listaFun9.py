#Entrada de dados
qtdP = int(input("Quantidade de camisas [P]: "))
qtdM = int(input("Quantidade de camisas [M]: "))
qtdG = int(input("Quantidade de camisas [G]: "))
#calculo e saida
valor = (qtdP * 10) + (qtdM * 12) + (qtdG * 15)
print(f"Valor a ser pago: {valor: .2f}")
