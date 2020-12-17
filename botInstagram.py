from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdrive.Firefox(executable_path=r'C:\Users\OPENDATA\Desktop\Lucas\Treinamentos Pessoais\Front-End\Youtube\Dev Aprender\Robo\Instagram\geckodriver.exe')

#URL para entrar
# https://www.instagram.com/accounts/login/

# XPATH do Trocar Conta
# /html/body/div[1]/section/main/div/div/div/div/div[3]/span/button
# de acordo com o video é //a[@href='/accounts/login/?source=auth_switcher']

#XPATH do INPUT
#
# de acordo com o video 
# //input[@name='username']
# //input[@name='password']

# Criando método do login
    driver = self.driver
    driver.get('https://www.instagram.com/accounts/login/')

lucasBot = InstagramBot('isso vai dominar o mundo','aindabemqueeuscriarum')
lucasbot.login()