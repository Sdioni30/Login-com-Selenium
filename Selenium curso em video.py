from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv
import os


load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")
SITE = os.getenv("SITE")

#identificar a versão do crhome atual e vai instalar o crhome driver correspondente a versão atual
servico1 = Service(ChromeDriverManager().install())

#Dizer a linha de codigo abaixo, que vamos usar o navegador que criei ou seja o "servico1", colocando ele dentro do webdriver.Chrome(coloque aqui) -->
navegador = webdriver.Chrome(service=servico1)


navegador.get("SITE")


navegador.find_element('xpath',
                    '//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[3]/input').send_keys(LOGIN)


navegador.find_element('xpath','//*[@id="uabb-password-field"]').send_keys(PASSWORD)

#clicar
navegador.find_element('xpath','//*[@id="post-42350"]/div/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/div/form/div[7]/div/button').click()
input('...')
