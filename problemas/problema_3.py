#Importando as funções
import os
from Sequencia import Sequencia
from OrganismoFasta import OrganismoFasta
from ler_fasta import ler_fasta

#Lendo o arquivo
diretorio_arquivo = os.path.join("arquivos", "Flaviviridae-genomes.fasta")
objetos_organismo = ler_fasta(diretorio_arquivo)

#Realizando a função
for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    nucleotideos = ["A", "T", "C", "G"]
    for nucleotideo in nucleotideos:
        percentual = organismo.sequencia.calcular_percentual(nucleotideo)
        print(f"Percentual de {nucleotideo}: {percentual * 100:.2f}%")

    percentual_GC = organismo.sequencia.calcular_percentual(["C", "G"])
    print(f"Conteúdo GC: {percentual_GC * 100:.2f}%")

    print()