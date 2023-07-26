def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal

altura_usuario = float(input("Digite sua altura em metros: "))


peso_ideal_usuario = calcular_peso_ideal(altura_usuario)


print("Seu peso ideal é:", peso_ideal_usuario, "kg")
