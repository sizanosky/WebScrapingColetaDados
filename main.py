"""
* Módulo 20 - Web Scraping
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 26/05/2021
  Programa em Python 3 para coletar dados de um website.
"""

import csv
from config import *
import requests
from bs4 import BeautifulSoup

"""
headers = {
    'User-Agent': '<product> / <product-version> <comment>',
    'From:': 'fabricio_sizanosky@hotmail.com'
}
"""

print("Hello World!!!\n")

paginas = []
for num_page in range(1, 5):
    paginas.append(f'https://web.archive.org/web/20121007172955/'
                   f'https://www.nga.gov/collection/anZ{num_page}.htm')

# Criando um arquivo.csv
arquivo_csv = csv.writer(open('nomes_artistas_z.csv', 'w', newline='\n'))
arquivo_csv.writerow(['Name_Artist', 'URL_artist'])  # Cabeçalho

for url_por_pagina in paginas:
    pagina = requests.get(url_por_pagina)  # ,headers=headers)
    soup = BeautifulSoup(pagina.text, 'html.parser')

    # Remover links inferiores.
    ultimos_links = soup.find(class_='AlphaNav')
    ultimos_links.decompose()

    # Pegar o conteúdo do body text.
    bloco_nome_artistas = soup.find(class_='BodyText')
    lista_nome_artistas = bloco_nome_artistas.find_all('a')  # tag 'a'

    for nome_artista in lista_nome_artistas:
        nomes = nome_artista.contents[0]  # iterando a tag filha[indice]
        links = f"{URL_BASE}{nome_artista.get('href')}"
        arquivo_csv.writerow([nomes, links])
        print(nomes)
        print(links)
