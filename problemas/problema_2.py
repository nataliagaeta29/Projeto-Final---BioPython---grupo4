import sys
import os

#add o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia

arquivo_fasta = 'arquivos/Flaviviridae-genomes.fasta'
objetos_organismo = ler_fasta(arquivo_fasta)

from bio.ler_fasta import ler_fasta

for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    sequencia_translate = organismo.sequencia.traduzir()
    print(f"Sequência de proteína: {sequencia_translate}")

    print()

