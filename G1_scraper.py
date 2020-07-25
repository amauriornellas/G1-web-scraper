print('::Importando Bibliotecas...') # Informação para o usuário

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import requests

from bs4 import BeautifulSoup



print('::Acessando o Navegador...') # Informação para o usuário

url = 'https://g1.globo.com/' # A url do Portal G1 que vamos acessar

option = Options() # Instanciando o Options para ocultar a abertura do navegador
option.headless = True # Esse comando quando True não abre o navegador e faz as operações no background

# Acessando o Google Chrome através do chromedriver na pasta que ele está instalado
# options=option faz carrega as especificações de abertura do navegador
driver = webdriver.Chrome('/Volumes/Armazenamento/Projetos/webscrapping/chromedriver', options=option)

print('::Aguardando a Página Carregar...') #Informação para o usuário

driver.get(url) # Informando o navegador o endereço que ele deve acessar

# Rolando a página até o final para carregar todas as manchetes
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(10) #Aguardando 10 segundos para ter todos os dados carregados

print('::Localizando as Manchetes...') # Informação para o usuário

# Encontrando o trecho da página que contém as manchetes e resumos e atribuindo à variável
element = driver.find_element_by_id("bstn-launcher")
html = element.get_attribute('outerHTML')

driver.quit() #Fecha o Navegador

soup = BeautifulSoup(html, 'lxml') #Interpretando o html

# Exibindo a data e a hora do acesso
print(time.strftime("\n::AS MANCHETES DO PORTAL G1 às %H:%M:%S do dia %d/%m/%Y::\n", time.localtime()))

# Encontra todas as manchetes e cria uma lista que é percorrida um a um
for article in soup.find_all(class_='feed-post-body'): 
    if article.a != None: # Checa se o formato está correto
        resumo = article.find(class_= 'feed-post-body-resumo') #Encontra o conteúdo do resumo do artigo
        print('* ', article.a.text) # Exibe o título do artigo
        if resumo != None: # Checa se existe resumo para o artigo
            print('  ', resumo.text) # Imprime o resumo
        print()
        