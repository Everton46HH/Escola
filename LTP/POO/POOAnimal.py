class Animal:
    def __init__(self,nome,especie):
        self.nome = nome
        self.especie = especie

    def setNome(self,nome):
        self.nome = nome

    def getNome(self):
        return self.nome

class Cachorro(Animal):
    def __init__(self,nome,especie,fazendoBagunca,mordendo,perseguindo):
        Animal.__init__(self,nome,especie)
        self.fazendoBagunca = fazendoBagunca
        self.mordendo = mordendo
        self.perseguindo = perseguindo

    def morderCoisas(self):
        self.fazendoBagunca = True

    def fazerBagunca(self):
        self.mordendo = False

    def perseguirGato(self,gato):
        self.perseguindo = gato
    
    
class Gato(Animal):
    def __init__(self,estado,comendo,fugindo,nome,especie):
        self.estado = estado
        self.comendo = comendo
        self.fugindo = fugindo
        Animal.__init__(self,nome,especie)

    def dormir(self):
        self.estado = True
    
    def comer(self):
        self.comendo = True
    
    def fugir(self,cachorro):
        self.fugindo = cachorro
    
    def fugindoDeQuem(self)
        return self.fugindo

gato1 = Gato("José","Bonitâo",0,0,0)


cachorro1 = Cachorro("Bagre","CãodeLabro",0,0,0)
cachorro1.perseguirGato(gato1)


print(gato1)