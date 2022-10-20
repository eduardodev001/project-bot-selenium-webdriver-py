import time
from selenium import webdriver


class BotWhatsapp:
    def __init__(self):
        self.mensagem = "Bot EduardoDev!"
        self.mensagemPersonalizada = "Olá, sou o bot do Eduardo Dev Nome: Eduardo E-mail= " \
                                     "eduardo.aquiles@uniuv.edu.br Telefone: 42991131652 "
        self.grupos = ["Recados"]
        opcoes = webdriver.ChromeOptions()
        opcoes.add_argument('lang=pt-br')
        self.caminho = webdriver.Chrome(executable_path=r'chromedriver.exe', chrome_options=opcoes)

    def MandarMensagens(self):
        # <span dir="auto" title="Algoritmos e estruturas I" class="_35k-1 _1adfa _3-8er">Algoritmos e estruturas
        # I</span> <div tabindex="-1" class="_2A8P4">

        # apontando o caminho do site
        self.caminho.get('https://web.whatsapp.com/')
        time.sleep(20)

        # Entrar no grupo
        grupo = self.caminho.find_element_by_xpath("//span[@title='Algoritmos e estruturas I']")
        time.sleep(3)
        grupo.click()

        # Entrar na caixa de texto
        campoTexto = self.caminho.find_element_by_class_name('_2A8P4')
        time.sleep(3)
        campoTexto.click()
        campoTexto.send_keys(self.mensagem)

        # <span data-testid="send" data-icon="send" class="">

        # enviar
        botaoEnviar = self.caminho.find_element_by_xpath("//span[@data-testid='send']")
        time.sleep(3)
        botaoEnviar.click()
        time.sleep(3)

    def LerMensagem(self):
        statusBot = True

        self.caminho.get('https://web.whatsapp.com/')
        time.sleep(20)

        grupo = self.caminho.find_element_by_xpath("//span[@title='Algoritmos e estruturas I']")
        time.sleep(3)
        grupo.click()

        while statusBot:

            retorno = self.caminho.find_element_by_xpath(
                '/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]').text
            listaRetorno = retorno.splitlines()

            if listaRetorno[len(listaRetorno) - 2] == "!EduardoDev":
                campoTexto = self.caminho.find_element_by_class_name('_2A8P4')
                time.sleep(3)
                campoTexto.click()
                campoTexto.send_keys(self.mensagemPersonalizada)

                # enviar
                botaoEnviar = self.caminho.find_element_by_xpath("//span[@data-testid='send']")
                time.sleep(3)
                botaoEnviar.click()

            time.sleep(10)