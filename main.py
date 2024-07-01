from bio.sequencia import Sequencia 

DNA = Sequencia ("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")

DNA.complementar()
print(DNA.complementar())

DNA.reverso_complementar()
print(DNA.reverso_complementar())

base_A = DNA.calcular_percentual(bases = ["A", "T", "C", "G"])
print(base_A) 

DNA.transcrever()
print(DNA.transcrever())

DNA.traduzir()
print(DNA.traduzir ())  
