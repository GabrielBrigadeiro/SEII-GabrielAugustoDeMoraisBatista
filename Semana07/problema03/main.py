# importando o App, Builder (GUI)
from kivy.app import App
from kivy.lang import Builder
import requests

GUI = Builder.load_file("tela.kv")

# criando o aplicativo
class MeuAplicativo(App):

    # criando a função build
    def build(self):
        return GUI

    # pegando moedas dinamicamente
    def on_start(self):
        self.root.ids["moeda1"].text = f"Dólar R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro  R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin  R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Ethereum R${self.pegar_cotacao('ETH')}"

    # pegando cotação
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

# executando o app
MeuAplicativo().run()