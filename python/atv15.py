import math

def calcular_latas_tinta(area):
    metros_por_lata = 18 * 3  # 1 litro para cada 3 metros quadrados
    latas_necessarias = math.ceil(area / metros_por_lata)
    preco_total = latas_necessarias * 80.00
    return latas_necessarias, preco_total

# Solicitar o tamanho da área a ser pintada em metros quadrados
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Chamar a função para calcular as latas de tinta e o preço total
latas_necessarias, preco_total = calcular_latas_tinta(area_a_ser_pintada)

# Exibir os resultados
print("Quantidade de latas de tinta a serem compradas:", latas_necessarias)
print("Preço total: R$", preco_total)
