class Tv:
    
    def __init__(self,canal,volume,ligada):
        self.canal = 0
        self.volume = 0
        self.ligada = False
    
    def ligar(self):
        self.ligada = True
        
    def desligar(self):
        self.ligada = False
        
    def setCanal(self,canal):
        self.canal = canal
        
    def setVolume(self,volume):
        self.volume = volume
    
    def isLigada(self):
        return self.ligada
    
    def setCanal(self,c):
        if c <= 0:
            self.canal = 0
        else:
            self.canal = c
        
    def getCanal(self):
        return self.canal
        
    def setVolume(self,v):
        if v > 100:
            self.volume = 100
        elif v <=0 :
            self.volume = 0
        else:
            self.volume = v
    
    def getVolume(self):
        return self.volume

tv1 = Tv(0,0,False)

tv1.setCanal(3)

tv1.setVolume(200)

print(tv1.isLigada())
print(tv1.getVolume())
print(tv1.getCanal())