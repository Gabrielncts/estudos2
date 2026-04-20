#entrada de dados e calculos
totalDias = int(input("Quantidade de dias sem acidentes: "))
anos = (totalDias / 360)
restoAnos = (totalDias % 360)
meses = (restoAnos / 30)
dias = (restoAnos % 30)
#saida
print(f"tempo convertido: {anos: .0f} ano(s), {meses: .0f} meses e {dias: .0f} dias" )