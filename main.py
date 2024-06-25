from bio.sequencia import Sequencia 

DNA = Sequencia ("ATCG")

DNA.complementar()
print(DNA.complementar())

DNA.reverso_complementar()
print(DNA.reverso_complementar())


DNA.transcrever()
print(DNA.transcrever())

base_A = DNA.calcular_percentual(bases = ["A", "C"])
print(base_A) 


