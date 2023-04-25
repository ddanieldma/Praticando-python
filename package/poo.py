# classe mae
class Animal:

    def comer(self):
        print("chomp chomp chomp")

    def dormir(self):
        print("zzzzzzzzzzZZzzzZzzZz")

# classe filha herdando classe mae animal


class Papagaio(Animal):

    # def comer(self):
    #     return super().comer()

    # def dormir(self):
    #     return super().dormir()

    def falar(self):
        print("não sei matematica basica")

# classe filha da filha herdando Papagaio


class Loro(Papagaio):

    # usando construtor, método que é chamado ao se instanciar um objeto
    def __init__(self, nome):
        self.nome = nome

    # def comer(self):
    #     return super().comer()
    # def dormir(self):
    #     return super().dormir()
    # def falar(self):
    #     return super().falar()


# criando primeiro objeto papagaio
papagaio_1 = Papagaio()

# chamando argumento classe mae
papagaio_1.comer()
papagaio_1.dormir()

# chamando argumentos novos
papagaio_1.falar()

# criando outro objeto papagaio
papagaio_2 = Papagaio()

# chamando argumento classe mae
papagaio_2.comer()
papagaio_2.dormir()

# chamando argumentos novos
papagaio_2.falar()

loro = Loro("Loro jose")

print(f"Meu nome é {loro.nome} eu ", end=" ")
loro.comer()
loro.dormir()
loro.falar()


class Produto:
    def __init__(self):
        # atributo privado
        self.__preco_maximo = 1000

    def vender(self):
        print("preço de venda {}".format(self.__preco_maximo))

    def setPrecoMaximo(self, novo_preco):
        self.__preco_maximo = novo_preco


produto = Produto()

# vendo preco
produto.vender()

# tentando mudar preco
produto.__preco_maximo = 9000
produto.vender()

# realmente mudando preco
produto.setPrecoMaximo(9000)
produto.vender()

# polimorfismo


class Poligono:
    # gerar um formato
    def gerar(self):
        print("gerando poligono...")


class Quadrado(Poligono):
    # gerar quadrado
    def gerar(self):
        print("gerando quadrado...")


class Circulo(Poligono):
    # gerar circulo
    def gerar(self):
        print("gerando circulo...")


# criando objeto de Quadrado
quadrado = Quadrado()
quadrado.gerar()

# criando objeto de Circulo
circulo = Circulo()
circulo.gerar()

# o mesmo método gerar existe de várias formas diferentes para duas subclasses
# de uma mesma superclasse, isso é o polimorfismo
