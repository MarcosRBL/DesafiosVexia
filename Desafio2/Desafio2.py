# Importação de bibliotecas
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Leitura do excel com os dados a serem preenchidos e trandormação em DataFrame
data = pd.read_excel('challenge.xlsx')
df = pd.DataFrame(data)

# Aponta o caminho do driver que controlará o navegador
service = Service(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Acessa o site para o desafio
driver.get("https://rpachallenge.com")

# Clica em "Start" para iniciar o desafio
inciarDesafio = driver.find_element(By.XPATH, "/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button").click()

# Faz o loop para cada linha do nosso DataFrame
for index, linhas in df.iterrows():
    # Preencimento do campo "First Name"
    nome = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelFirstName']")
    nome.send_keys(linhas[0])
    time.sleep(0.5)
    # Preencimento do campo "Last Name"
    sobrenome = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelLastName']")
    sobrenome.send_keys(linhas[1])
    time.sleep(0.5)
    # Preencimento do campo "Company Name"
    empresa = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelCompanyName']")
    empresa.send_keys(linhas[2])
    time.sleep(0.5)
    # Preencimento do campo "Role in Company"
    cargo = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelRole']")
    cargo.send_keys(linhas[3])
    time.sleep(0.5)
    # Preencimento do campo "Address"
    endereco = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelAddress']")
    endereco.send_keys(linhas[4])
    time.sleep(0.5)
    # Preencimento do campo "Email"
    email = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelEmail']")
    email.send_keys(linhas[5])
    time.sleep(0.5)
    # Preencimento do campo "Phone Number"
    telefone = driver.find_element(By.XPATH, "//*[@ng-reflect-name='labelPhone']")
    telefone.send_keys(linhas[6])
    time.sleep(0.5)
    # Clica no botão "Submit"
    submit = driver.find_element(By.XPATH, "//*[@value='Submit']").click()
    time.sleep(0.5)

# Após o loop ele fecha o navegador
time.sleep(6)
driver.quit()