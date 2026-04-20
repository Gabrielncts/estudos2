#entrada e calculo
salario = float(input("Digite o salario inicial do funcionario: "))
salarioAumento = (salario * 1.15)
    #saida com atualizacao do processo
print(f"Salario com aumento: {salarioAumento: .3f}")
print("imposto de 8% aplicado! ")
salarioFinal = (salarioAumento * 0.92)
    #saida
print(f"Salario final: {salarioFinal: .3f} reais")

