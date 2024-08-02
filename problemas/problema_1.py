import sys
import os

#add o diretório do projeto ao sys.path
diretorio_arquivo = sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath("Flaviviridae-genomes.fasta"))))
objetos_organismo = ler_fasta(diretorio_arquivo)


from bio.ler_fasta import ler_fasta

for organismo in objetos_organismo:
    print(f"Organismo: {organismo.id}")

    nucleotideos = ["A", "T", "C", "G"]
    for nucleotideo in nucleotideos:
        percentual = organismo.sequencia.calcular_percentual(nucleotideo)
        print(f"Percentual de {nucleotideo}: {percentual * 100:.2f}%")

    percentual_GC = organismo.sequencia.calcular_percentual(["C", "G"])
    print(f"Conteúdo GC: {percentual_GC * 100:.2f}%")

    print()