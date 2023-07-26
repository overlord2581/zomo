def calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps):
    tamanho_arquivo_bits = tamanho_arquivo_mb * 8 * 1024 * 1024  # Converter MB para bits
    tempo_segundos = tamanho_arquivo_bits / (velocidade_internet_mbps * 1024 * 1024)  # Converter para Mbps
    tempo_minutos = tempo_segundos / 60
    return tempo_minutos

# Solicitar o tamanho do arquivo para download (em MB) e a velocidade da Internet (em Mbps)
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
velocidade_internet_mbps = float(input("Digite a velocidade da Internet (em Mbps): "))

# Chamar a função para calcular o tempo aproximado de download
tempo_minutos = calcular_tempo_download(tamanho_arquivo_mb, velocidade_internet_mbps)

# Exibir o resultado
print("O tempo aproximado de download é de:", round(tempo_minutos, 2), "minutos")
