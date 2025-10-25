######### EXercicio 1 ###############
#Crie uma classe Retangulo que receba largura e altura.
#Métodos: area() e perimetro().
#Teste criando ao menos dois retângulos com dimensões diferentes e imprima área e perímetro.
import math


class Retangulo():
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

Objeto1 = Retangulo(5, 5)
Objeto2 = Retangulo(20, 5)
print(Objeto1.area())
print(Objeto2.area())
print(Objeto1.perimetro())
print(Objeto2.perimetro())


######### EXercicio 2 ###############
#Classe Circulo que receba raio.
#Métodos: area() e circunferencia().
#se math.pi para π. Crie um círculo de raio 5 e mostre resultados.

class Circulo():
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return math.pow(self.raio,2) * math.pi

    def circunferencia(self):
        return 2 * self.raio * math.pi


Objeto3 = Circulo(5)
print(Objeto3.area())
print(Objeto3.circunferencia())

######### EXercicio 3 ###############
#Classe Livro com atributos título, autor e ano_publicacao.
#Implemente o método mágico __str__ para retornar algo como "'Dom Casmurro', de Machado de Assis (1899)".
#Instancie e faça print(livro).

class Livro():
    def __init__(self,titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao


    def __str__(self):
        return f"'{self.titulo}', de {self.autor} ({self.ano_publicacao})"

livro1 = Livro('Dom Casmurro', 'Machado de Assis', 1899)
print(livro1)

######### EXercicio 4 ###############
#Classe Aluno com nome e lista de notas (inicialmente vazia).
#Métodos: adicionar_nota(valor) e media().
#Crie um aluno, adicione pelo menos 3 notas e exiba a média.

class Aluno():
    def __init__(self,nome):
        self.nome = nome
        self.notas = []

    def adicioanr_nota(self, valor):
        self.notas.append(valor)
        return self.notas

    def media(self):
        return sum(self.notas)/len(self.notas)

aluno1 = Aluno('Guilherme')
aluno1.adicioanr_nota(10)
aluno1.adicioanr_nota(10)
aluno1.adicioanr_nota(10)
print(aluno1.media())

######### EXercicio 5 ###############
#A partir da sua ContaBancaria, adicione um atributo de classe banco (por exemplo, "Banco XYZ").
#Implemente @classmethod alterar_banco(novo_nome).
#Verifique que mudar via classe reflete em todas as instâncias.

class ContaBancaria:
    banco = "Banco XYZ"
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, valor):
        self.saldo += valor
        return self.saldo
    @classmethod
    def alterar_banco(cls,novo_nome):
        cls.banco = novo_nome


    def sacar(self, valor):
        self.saldo -= valor
        return self.saldo

    def mostrar_saldo(self):
        return self.saldo

banco1 = ContaBancaria("Guilherme",5000)
ContaBancaria.alterar_banco('Santander')
print(banco1.banco)