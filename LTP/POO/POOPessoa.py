class Pessoa:
    def __init__(self):
        self.nome = None
        self.cpf = None
    def setNome(self, novoNome):
        self.nome = novoNome
    def setCpf(self, novoCpf):
        self.cpf = novoCpf

class Aluno(Pessoa):
        def __init__(self):
            Pessoa.__init__(self)
            self.curso = None
            self.prontuario = None
        def setCurso(self, curso):
            self.curso = curso
        def setProntuario(self, curso):
            self.curso = curso

pessoa1 = Pessoa ()
aluno1 = Aluno()
pessoa1.setNome("José Silva")
aluno1.setCpf(123456789)
aluno1.setCurso("Técnico em Informática")
print(pessoa1.nome)
print(aluno1.cpf)
print(aluno1.curso)

# 1. Crie uma classe chamada Ingresso, que possui um valor em reais e um método getValor() –

# – Crie uma classe VIP, que herda de Ingresso e possui um valor adicional. Crie um método que retorne o valor do ingresso VIP (com o adicional incluído) 

# 2. Crie uma classe chamada Forma, que possui os atributos area e perimetro.

# – Implemente as subclasses Retangulo e Triangulo, que devem conter os métodos calculaArea e calculaPerimetro.

# A classe Triangulos deve ter também o atributo altura. 

# No código de teste crie um objeto da classe Triangulo e outro da Classe Retangulo e calcule a área de cada um. 