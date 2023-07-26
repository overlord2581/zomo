def calcular_peso_ideal(altura, genero):
    if genero == 'homem':
        peso_ideal = (72.7 * altura) - 58
    elif genero == 'mulher':
        peso_ideal = (62.1 * altura) - 44.7
    else:
        print("Gênero não reconhecido. Use 'homem' ou 'mulher'.")
        return None
    return peso_ideal

# Solicitar a altura e gênero do usuário
altura_usuario = float(input("Digite sua altura em metros: "))
genero_usuario = input("Digite seu gênero (homem/mulher): ").lower()

# Chamar a função para calcular o peso ideal
peso_ideal_usuario = calcular_peso_ideal(altura_usuario, genero_usuario)

# Exibir o resultado, se o gênero for válido
if peso_ideal_usuario is not None:
    print("Seu peso ideal é:", peso_ideal_usuario, "kg")
