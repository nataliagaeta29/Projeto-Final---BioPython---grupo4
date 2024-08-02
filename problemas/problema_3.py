
import sys
import os

#add o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
objetos_organismo = ler_fasta(arquivo_fasta)

from bio.ler_fasta import ler_fasta

#aplicando a função

for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    sequencia = organismo.sequencia
    nucleotideo_1000 = sequencia[999]
    mutacao_presente = False
    
    if nucleotideo_1000 == "G":
        mutacao_presente = True

    if mutacao_presente:
        print("A mutação está presente na posição 1000.")
    else:
        print("A mutação não está presente na posição 1000.")
    
    print()
