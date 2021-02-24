from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
    executable_path=os.getcwd() + os.sep + 'geckodriver.exe')
       

# Criando método do login
    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com')
        time.sleep(2)
        try:
            login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
            login_button.click()
        except:
            print('Já estamons na página de login')
            pass
        user_element = driver.find_element_by_xpath("//input[@name='username']")
        user_element.clear()
        time.sleep(random.randint(4,6))
        user_element.send_keys(self.username)
        time.sleep(random.randint(4,6))
        password_element = driver.find_element_by_xpath("//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(random.randint(4,6))
        password_element.send_keys(Keys.RETURN)
        time.sleep(random.randint(4,7))
        self.curtir_fotos_com_a_hashtag("skate") # Alterar a hashtag aqui

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        #Simulando como uma pessoa digita
        print("Começarei a digitar uma mensagem, na area da mensagem")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def curtir_fotos_com_a_hashtag(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)
        for i in range(1, 3): # Alterar aqui a quantidade de páginas para descer
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        hrefs = driver.find_elements_by_tag_name("a")
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + " fotos: " + str(len(pic_hrefs)))
        testes = [
            href
            for href in pic_hrefs
            if hashtag in href and href.index("https://www.instagram.com/programa") != -1
        ]

        for pic_href in pic_hrefs:
            try:
                pic_href.index("https://www.instagram.com/p")
            except ValueError as err:
                print("Pulando link inválido!")
                continue
            driver.get(pic_href)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                #driver.find_element_by_class_name('//button[@class="_9AhH0"')
                #time.sleep(10)
                
                #driver.find_element_by_class_name("wpO6b").click()
                #driver.find_elements_by_css_selector(".eos2AS section span button").click()
                driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[1]/span[1]/button")
               # driver.find_element_by_xpath("//span[@class='fr66n']").click() 

                driver.find_element_by_class_name("eo2As").find_element_by_class_name("ltpMr").find_element_by_class_name("fr66n").find_element_by_tag_name("button").click()
                time.sleep(random.randint(19,23))
                #curtir_element.send_keys(Keys.RETURN)
               # time.sleep(random.randint(19, 32))
            except Exception as e:
                print(e)

                time.sleep(5)




lucasBot = InstagramBot('lucas.conceicao97@hotmail.com','Moreko301015[]') # Usuário e senha aqui
lucasBot.login()