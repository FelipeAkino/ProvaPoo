from Classes import ContaLuz,Contas

historiContas = Contas()

historiContas.addContaLuz(ContaLuz("125","001",150))
historiContas.addContaLuz(ContaLuz("125","002",175))
historiContas.addContaLuz(ContaLuz("125","003",190))
historiContas.addContaLuz(ContaLuz("125","004",150))
print(historiContas.mediaConsumoValor())