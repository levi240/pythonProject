import time
import csv,json
import requests
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import shutil
navegador = webdriver.Chrome()
def abre_pagina():
    navegador.get("https://opendatasus.saude.gov.br")
    navegador.find_element(By.XPATH, '//*[@id="main-navigation-toggle"]/nav/ul/li[1]/a').click()
    navegador.find_element(By.XPATH, '// *[ @ id = "content"] / div[3] / div / section[1] / div / ul / li[1] / div / h3 / a').click()
    navegador.find_element(By.XPATH, '// *[ @ id = "dataset-resources"] / ul / li[3] / a').click()
    navegador.find_element(By.XPATH, '// *[ @ id = "content"] / div[3] / section / div / p / a').click()

def move_arquivo():
    source = r'C:\Users\user\Downloads\esus-vepi.LeitoOcupacao_2020.csv'
    destination = r'C:\Users\user\OneDrive\Documentos\repositorio\dados_covid19'
    try:
        shutil.move(source, destination)
    except FileNotFoundError as error:
        print(error)
    except:
        print("Erro desconhecido")
        shutil.move(source, destination)
    else:
        print("Arquivo movido com sucesso")
    navegador.close()

def ler_arquivo():
    diretorio=r"C:\Users\user\OneDrive\Documentos\repositorio\dados_covid19\esus-vepi.LeitoOcupacao_2020.csv"
    with open(diretorio,"r") as arquivo:
        arquivo_csv=csv.reader(arquivo,delimiter=",")
        for i in enumerate(arquivo_csv):
            print(i)


#abre_pagina()
#time.sleep(40)
#move_arquivo()
ler_arquivo()