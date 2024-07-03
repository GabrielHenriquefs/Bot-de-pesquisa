import requests
from bs4 import BeautifulSoup

# Função para realizar a pesquisa no Google e extrair os resultados
def busca_google(termo_pesquisa, num_resultados=10):
    # URL de busca no Google com o termo de pesquisa e o número de resultados desejado
    url_busca = f"https://www.google.com/search?q={termo_pesquisa}&num={num_resultados}"

    # Cabeçalho HTTP para a requisição, para evitar bloqueios simulando um navegador
    cabecalho = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    # Faz a requisição HTTP para o URL de busca
    resposta = requests.get(url_busca, headers=cabecalho)
    resposta.raise_for_status()  # Garante que a requisição foi bem-sucedida

    # Analisa a resposta HTML com BeautifulSoup
    sopa = BeautifulSoup(resposta.text, 'html.parser')

    resultados = []  # Lista para armazenar os resultados extraídos

    # Encontra todos os elementos div que contêm os textos dos resultados da busca
    for g in sopa.find_all('div', class_='BNeawe s3v9rd AP7Wnd'):
        if g.text and g.text not in resultados:  # Verifica se o texto não é vazio e não está duplicado
            resultados.append(g.text)  # Adiciona o texto à lista de resultados

    # Retorna a quantidade de resultados especificada
    return resultados

# Função para formatar os resultados em um texto contínuo com no mínimo 150 palavras
def formatar_resultados(resultados):
    texto_formatado = ""
    palavras = 0
    for resultado in resultados:
        texto_formatado += resultado + " "
        palavras += len(resultado.split())
        if palavras >= 150:
            break
    return texto_formatado





# Termo de pesquisa
termo_pesquisa = "south park"


# Realiza a pesquisa no Google
resultados_pesquisa = busca_google(termo_pesquisa)

# Formata e exibe os resultados
if resultados_pesquisa:
    texto_formatado = formatar_resultados(resultados_pesquisa)
    print(texto_formatado)  # Imprime o texto formatado
else:
    # Mensagem caso nenhum resultado seja encontrado
    print("Nenhum resultado encontrado.")
