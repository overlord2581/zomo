def calcular_salario_liquido(ganho_por_hora, horas_trabalhadas):
    salario_bruto = ganho_por_hora * horas_trabalhadas
    ir = salario_bruto * 0.11
    inss = salario_bruto * 0.08
    sindicato = salario_bruto * 0.05
    salario_liquido = salario_bruto - (ir + inss + sindicato)
    return salario_bruto, ir, inss, sindicato, salario_liquido

# Solicitar o valor ganho por hora e o número de horas trabalhadas no mês
ganho_por_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

# Chamar a função para calcular o salário líquido
salario_bruto, ir, inss, sindicato, salario_liquido = calcular_salario_liquido(ganho_por_hora, horas_trabalhadas)

# Exibir os resultados
print("+ Salário Bruto : R$", salario_bruto)
print("- IR (11%) : R$", ir)
print("- INSS (8%) : R$", inss)
print("- Sindicato (5%) : R$", sindicato)
print("= Salário Líquido : R$", salario_liquido)
