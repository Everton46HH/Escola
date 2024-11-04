# Classe Mãe
class Ingresso():
    def __init__(self,valor):
        self.valor = valor

    # Valor do Ingresso
    def toString(self):
        return self.valor
    

# Classe Filha

class IngressoVip(Ingresso):
    def __init__(self,valor,valorAdc):
        Ingresso.__init__(self)
        self.valorAdc = valorAdc
    # Retorna o valor o valor total do IngressoVip
    def toString(self):
        return self.valor + self.valorAdc

Ingresso1 = Ingresso(40)
IngressoVip1 = IngressoVip(40,50)

print(f"O valor do Ingresso é : {Ingresso1.toString()}")
print(f"O valor do IngressoVip é : {IngressoVip1.toString()}")