import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from datetime import date, timedelta
import time
navegador = webdriver.Chrome()

def enterSite():
    navegador.get("https://www.caixa.gov.br/Paginas/home-caixa.aspx")
    #time.sleep(3)
    navegador.find_element(By.XPATH, '//*[@id="botao"]/button').click()
    navegador.find_element(By.XPATH, '//*[@id="content-menu"]/ul/li[4]/a').click()
    #time.sleep(3)
    navegador.find_element(By.ID, 'ctl00_ctl59_g_16298322_5739_4d08_bcc7_b4e9dea4c93a_LinkButtonMaisLoterias').click()
    navegador.find_element(By.XPATH, '// *[ @ id = "ctl48_g_02bfeca0_05ba_4876_bea5_5efdfa91f8e3"] / div / div[2] / div[2] / div[2] / p[2] / a').click()

def resultadoMegasena():
    html =requests.get('https://loterias.caixa.gov.br/Paginas/Mega-Sena.aspx').content
    soup = BeautifulSoup(html, 'html.parser')
    resultado = soup.find('span', class_='ng-binding')
    print(resultado)


enterSite()
resultadoMegasena()
#dt_inicio=date.today()
#print(dt_inicio.strftime("%d/%m/%Y"))
#print(dt_inicio.isoformat(timespec='microseconds'))
#navegador.find_element(By.XPATH, '//*[@id="conteudo-principal"]/div[4]/div[3]/div/div[2]/ul/li[5]/a/div/h2').click()
#dt_cotacao = navegador.find_element(By.XPATH, '*[@id="wrapper"]/div/div/div/div[2]/div[1]/div/div[1]/a/div/div/div').text
#print(dt_cotacao)



#navegador.find_element(By.XPATH, '/html/body/form/main/div[2]/div/div/div[2]/div/div[2]/div/div/div[2]/div/div/a[1]').click()
#time.sleep(3)
#navegador.find_element(By.XPATH, '//*[@id="icon"]/iron-icon').click()
#navegador.close()


