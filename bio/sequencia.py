class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)
    
    
    def complementar(self):
        complementar = {
            'A':'T', 
            'T':'A', 
            'C':'G', 
            'G':'C'
            }
        sequencia_complementar = ""

        for base in self.sequencia:
            sequencia_complementar += complementar[base]
        return Sequencia(sequencia_complementar)
    
    
    def reverso_complementar(self):
        complementar = {
            'A':'T', 
            'T':'A', 
            'C':'G', 
            'G':'C'
            }
        sequencia_complementar = ""
        
        for base in self.sequencia:
            sequencia_complementar += complementar[base]
            reverso_complemento = sequencia_complementar[::-1]
        return Sequencia(reverso_complemento)
    

    def transcrever(self):
        transcrito = {
            'A':'U', 
            'T':'A', 
            'C':'G', 
            'G':'C'
            }
        sequencia_transcrita = ""

        for base in self.sequencia:
            sequencia_transcrita += transcrito[base]
        
        return Sequencia(sequencia_transcrita)
    

    def calcular_percentual(self, bases): #Muitas partes pensei sozinha, mas algumas o chatGPT me ajudou galera..
            comprimento_sequencia = len(self.sequencia)
            percentual = {}
        
            for base in bases:
                contagem_base = self.sequencia.count(base)
                percentual[base] = (contagem_base / comprimento_sequencia) * 100
        
            return percentual
        