from bs4 import BeautifulSoup
import requests


html = requests.get("https://b2c.voegol.com.br/compra/selecao-de-voo/ida").content
soup = BeautifulSoup(html, 'html.parser')
print(soup.prettify())
#maxTemp = soup.find("span",id="max-temp-1")
#minTemp = soup.find("span",id="min-temp-1")
#print(f"Amanha a máxima é de {maxTemp.string} e a minima de {minTemp.string}")