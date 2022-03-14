from bs4 import BeautifulSoup
import requests


site = requests.get('https://www.climatempo.com.br/').content

soup = BeautifulSoup(site, 'html.parser')



print(soup.prettify())

#Objeto site recebe o conteudo da requissicao http do site
#objeto soup ele esta baixando do site o html
# o prettify transforma o hatml em string para ser exibido pelo print