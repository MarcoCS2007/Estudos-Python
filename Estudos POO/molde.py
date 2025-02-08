#001 - Questão elaborada por Gemini - Crie uma classe chamada Carro com os seguintes atributos: marca, modelo, ano e cor. Crie um método chamado start que imprime a mensagem "O carro está ligando." Crie um método chamado stop que imprime a mensagem "O carro está desligando." Crie um objeto da classe Carro e chame os métodos start e stop.

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def stop(self):
        print(f'O {self.marca} {self.modelo} está desligando')

    def start(self):
        print(f'O {self.marca} {self.modelo} está ligando')

#002 - Questão elaborada por Gemini - Crie uma classe chamada Animal com os seguintes atributos: nome, espécie e idade. Crie um método chamado make_sound que imprime o som que o animal faz. Crie um método chamado eat que imprime a mensagem "O animal está comendo." Crie objetos da classe Animal para diferentes animais (por exemplo, cachorro, gato, pássaro) e chame os métodos make_sound e eat para cada objeto.

class Animal:

    def __init__(self, nome, espécie, idade):
        self.nome = nome
        self.idade =  idade
        self.especie = espécie
    
    def make_sound(self):
        print (f'O {self.especie} faz {self.animal_sound()}')
    
    def eat(self, comida = ('')):
        print(f'O {self.especie} está comendo {comida}.')
    
    def animal_sound(self):
        if self.especie == 'Gato':
            return 'miauu'
        elif self.especie == 'Cachorro':
            return 'au au'
        elif self.especie == 'Pássaro':
            return 'piu piu'
        else:
            return 'Som desconhecido'
        
#003 - Questão elaborada por Gemini - Crie uma classe chamada ContaBancaria com os seguintes atributos: numero_da_conta, saldo e proprietario. Crie um método chamado depositar que adiciona dinheiro ao saldo da conta. Crie um método chamado sacar que subtrai dinheiro do saldo da conta. Crie um objeto da classe ContaBancaria e chame os métodos depositar e sacar.

class ContaBancaria:
    def __init__(self, numero_da_conta, saldo, propietario):
        self.numero_da_conta = numero_da_conta
        self.saldo = saldo
        self.propietario = propietario

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print (f'Valor indisponivel no saldo!\nSaldo atual: {self.saldo}')

#004 - Questão elaborada por Gemini - Crie uma classe chamada Pessoa com os seguintes atributos: primeiro_nome, ultimo_nome e idade. Crie um método chamado nome_completo que retorna o nome completo da pessoa. Crie um método chamado is_adulto que retorna True se a pessoa tiver 18 anos ou mais, e False caso contrário. Crie um objeto da classe Pessoa e chame os métodos nome_completo e is_adulto.

class pessoa:

    def __init__(self, primeiro_nome, ultimo_nome, idade):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = ultimo_nome
        self.idade = idade

    def nome_completo(self):
        return f'{self.primeiro_nome} {self.sobrenome}'
    
    def is_adult(self):
        if self.idade >= 18:
            return True
        else:
            return False
        
#005 - Questão elaborada por Gemini - Crie uma classe chamada Forma com o seguinte atributo: cor. Crie um método chamado get_area que retorna a área da forma. Crie subclasses de Forma para diferentes formas (por exemplo, Circulo, Retangulo, Triangulo) e sobrescreva o método get_area em cada subclasse para calcular a área da forma específica.

...

#006 - Questão elaborada por Marco - Utilizando a classe Pessoa do exercício #004, adicione um metodo de classe que leia da data de nascimento ao inves da idade e retorne ao objeto principal a idade, baseando-se no ano atual.

class pessoa_update:

    from datetime import datetime

    ano_atual = ano_atual = datetime.now().year

    def __init__(self, primeiro_nome, ultimo_nome, idade):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = ultimo_nome
        self.idade = idade

    def nome_completo(self):
        return f'{self.primeiro_nome} {self.sobrenome}'
    
    def is_adult(self):
        if self.idade >= 18:
            return True
        else:
            return False

    @classmethod
    def get_ano_nascimento(cls, primeiro_nome, ultimo_nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(primeiro_nome, ultimo_nome, idade)

#007 - Questão elaborada por Marco - Utilizando a classe Pessoa do exercício #006, adicione um metodo etsático que gere um id para o objeto.

class pessoa_update_2:

    from datetime import datetime

    ano_atual = ano_atual = datetime.now().year

    def __init__(self, primeiro_nome, ultimo_nome, idade):
        self.primeiro_nome = primeiro_nome
        self.sobrenome = ultimo_nome
        self.idade = idade

    def nome_completo(self):
        return f'{self.primeiro_nome} {self.sobrenome}'
    
    def is_adult(self):
        if self.idade >= 18:
            return True
        else:
            return False

    @classmethod
    def get_ano_nascimento(cls, primeiro_nome, ultimo_nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(primeiro_nome, ultimo_nome, idade)
    
    @staticmethod
    def gerar_id():
        from random import randint

        id = randint(10000, 99999)
        return id
    
#008 - Questão elaborada por Marco - Crie uma classe chamada 'Produto', que receba os valores 'nome' e 'preco' e adicione um método que aplique um desconto percentual ao produto. configure para que o nome tenha a primeira letra maiuscula e o restante minuscula e para que o preço possa sempre ser lido como int ou float.

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome.strip().title()

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, preco):
        if isinstance(preco, str):
            preco = preco.replace(',', '.')
            for caracter in preco:
                if caracter not in '123456789.':
                    preco = preco.replace(caracter, '')
            if preco[0] == '.':
                preco = preco.replace('.', '')
        self._preco = float(preco)
    
    def desconto(self,percentual):
        return self.preco - self.preco/100*percentual 
    
    