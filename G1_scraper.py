print('::Importando Bibliotecas...')  # Informação para o usuário

from utils.functions import browserOptionSwitcher
import time
import requests
from bs4 import BeautifulSoup

browserOption = int(input("Escolha o navegador:\n1 - Firefox\n2 - Chrome\n"))

driver = browserOptionSwitcher(browserOption)

print('::Acessando o Navegador...')  # Informação para o usuário

url = 'https://g1.globo.com/'  # A url do Portal G1 que vamos acessar

print('::Aguardando a Página Carregar...')  # Informação para o usuário

driver.get(url)  # Informando o navegador o endereço que ele deve acessar

# Rolando a página até o final para carregar todas as manchetes
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)  # Aguardando 10 segundos para ter todos os dados carregados

print('::Localizando as Manchetes...')  # Informação para o usuário

# Encontrando o trecho da página que contém as manchetes e resumos e atribuindo à variável
element = driver.find_element_by_id("bstn-launcher")
html = element.get_attribute('outerHTML')

driver.quit()  # Fecha o Navegador

soup = BeautifulSoup(html, 'lxml')  # Interpretando o html

# Exibindo a data e a hora do acesso
print(time.strftime("\n::AS MANCHETES DO PORTAL G1 às %H:%M:%S do dia %d/%m/%Y::\n", time.localtime()))

# Encontra todas as manchetes e cria uma lista que é percorrida um a um
for article in soup.find_all(class_='feed-post-body'):
    if article.a is not None:  # Checa se o formato está correto
        resumo = article.find(class_='feed-post-body-resumo')  # Encontra o conteúdo do resumo do artigo
        print('* ', article.a.text)  # Exibe o título do artigo
        if resumo is not None:  # Checa se existe resumo para o artigo
            print('  ', resumo.text)  # Imprime o resumo
        print()
