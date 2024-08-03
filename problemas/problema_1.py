import sys
import os

#add o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

arquivo_fasta = './arquivos/Flaviviridae-genomes.fasta'
objetos_organismo = ler_fasta(arquivo_fasta)


for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    nucleotideos = ["A", "T", "C", "G"]
    for nucleotideo in nucleotideos:
        percentual = organismo.sequencia.calcular_percentual(nucleotideo)
        print(f"Percentual de {nucleotideo}: {percentual}")

    percentual_GC = organismo.sequencia.calcular_percentual(["C", "G"])
    print(f"Conteúdo GC: {percentual_GC}")

    print()