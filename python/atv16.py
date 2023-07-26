import math

def calcular_compra_tinta(area):
    litros_necessarios = area / 6  # 1 litro para cada 6 metros quadrados
    litros_necessarios_com_folga = litros_necessarios * 1.10  # 10% de folga
    latas_necessarias = math.ceil(litros_necessarios_com_folga / 18)
    galoes_necessarios = math.ceil(litros_necessarios_com_folga / 3.6)
    
    preco_apenas_latas = latas_necessarias * 80.00
    preco_apenas_galoes = galoes_necessarios * 25.00
    
    # Misturar latas e galões para minimizar o desperdício
    litros_restantes_latas = litros_necessarios_com_folga % 18
    latas_necessarias_mix = latas_necessarias
    if litros_restantes_latas > 0:
        latas_necessarias_mix += 1
        galoes_necessarios_mix = 0
    else:
        galoes_necessarios_mix = galoes_necessarios
    
    preco_mistura = (latas_necessarias_mix * 80.00) + (galoes_necessarios_mix * 25.00)
    
    return latas_necessarias, galoes_necessarios, preco_apenas_latas, preco_apenas_galoes, preco_mistura

# Solicitar o tamanho da área a ser pintada em metros quadrados
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Chamar a função para calcular as quantidades de tinta e os preços em três situações
latas_necessarias, galoes_necessarios, preco_apenas_latas, preco_apenas_galoes, preco_mistura = calcular_compra_tinta(area_a_ser_pintada)

# Exibir os resultados
print("Situação 1: Comprar apenas latas de 18 litros")
print("Quantidade de latas: ", latas_necessarias)
print("Preço total: R$", preco_apenas_latas)
print()

print("Situação 2: Comprar apenas galões de 3,6 litros")
print("Quantidade de galões: ", galoes_necessarios)
print("Preço total: R$", preco_apenas_galoes)
print()

print("Situação 3: Misturar latas e galões")
print("Quantidade de latas: ", latas_necessarias)
print("Quantidade de galões: ", galoes_necessarios)
print("Preço total: R$", preco_mistura)
