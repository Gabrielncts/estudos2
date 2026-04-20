dia = int(input("informe o dia: "))
mes = int(input("informe o mes: "))

# calculo dos dias
diasPassados = (mes - 1) * 30 + dia

#saida
print(f"Passaram {diasPassados} dias desde o inicio do ano")