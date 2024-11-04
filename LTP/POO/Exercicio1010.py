from abc import ABC, abstractmethod

class Veiculo(ABC):

    def __init__(self,placa,combustivel,quilometragem,alugado,precoDiaria):
        self.placa = placa
        self.combustivel = combustivel
        self.quilometragem = quilometragem
        self.alugado = False
        self.precoDiaria = precoDiaria
    
    def setGasolina(AddGasolina):
        self.gasolina += AddGasolina
    
    def toString(self):
        return f"A placa é : {self.placa}\nO nível do combutivel:{self.combustivel}\nQuilometragem : {self.quilometragem}\nO está alugado? : {self.alugado}\nO preco da diaria : {self.precoDiaria}"
    
    def equals():
        pass
    
    @abstractmethod

    def setViajar():
        pass

class Moto(veiculo):
    def __init__(self,placa,combustivel,quilometragem,alugado,precoDiaria):
        super().__init__(self,placa,combustivel,quilometragem,alugado,precoDiaria)


# O método abastecer deve adicionar o valor passado por parâmetro ao atributo combustivelNoTanque 
# O método equals deve retornar true se o valor do atributo placa for o mesmo para os dois objetos. 

# Método viajar - Moto: o método deve considerar que uma moto faz 30km com 1 litro de combustível. Logo, 
# deve verificar se o combustível no tanque é suficiente para percorrer a distância passada como parâmetro
# do método. Caso seja, deverá reduzir essa quantidade do atributo combustívelNoTanque e adicionar o valor 
# da distância ao valor do atributo quilometragem. Retorne o valor true caso seja possível realizar a viagem. 
# Caso contrário, retorne false 

# Método viajar - Carro: Deve considerar que um carro faz 10km com um litro de combustível. Fazer as mesmas 
# operações que as descritas no método viajar da classe Moto. 