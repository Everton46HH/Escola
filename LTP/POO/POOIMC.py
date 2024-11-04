from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def calcularImc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def fazerAniversario(self):
        self.idade += 1
        print(f"Parabéns! {self.nome} agora tem {self.idade} anos.")

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos, {self.altura}m de altura e peso {self.peso}kg.")

    @abstractmethod
    def pesoIdeal(self):
        pass

class Homem(Pessoa):
    def __init__(self, nome, idade, altura, peso):
        super().__init__(nome, idade, altura, peso)

    def pesoIdeal(self):
        return 72.7 * self.altura - 58


class Mulher(Pessoa):
    def __init__(self, nome, idade, altura, peso):
        super().__init__(nome, idade, altura, peso)

    def pesoIdeal(self):
        return 62.1 * self.altura - 44.7

h = Homem("Pedro", 20, 1.78, 100)
m = Mulher("Ana", 20, 1.50, 40)

h.apresentar()
print("Peso ideal: ", h.pesoIdeal())


m.apresentar()
print("Peso ideal: ", m.pesoIdeal())
