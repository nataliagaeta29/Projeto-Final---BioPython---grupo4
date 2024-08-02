import sys
import os

#add o diretório do projeto ao sys.path
diretorio_arquivo = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("Flaviviridae-genomes.fasta"))))

objetos_organismo = ler_fasta(diretorio_arquivo)
from bio.ler_fasta import ler_fasta

for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    sequencia_translate = organismo.sequencia.traduzir()
    print(f"Sequência de proteína: {sequencia_translate}")

    print()

