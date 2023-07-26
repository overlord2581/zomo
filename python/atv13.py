def calcular_multa(peso_peixes):
    limite_peso = 50  # Limite estabelecido pelo regulamento (em quilos)
    excesso = max(peso_peixes - limite_peso, 0)
    multa = excesso * 4.00
    return excesso, multa

# Solicitar o peso de peixes ao usuário
peso_peixes = float(input("Digite o peso de peixes em quilos: "))

# Chamar a função para calcular o excesso e a multa
excesso, multa = calcular_multa(peso_peixes)

# Exibir os resultados
if excesso == 0:
    print("Não há excesso de peso. Não é necessário pagar multa.")
else:
    print("Excesso de peso:", excesso, "quilos")
    print("Valor da multa a pagar: R$", multa)
