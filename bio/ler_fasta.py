from bio.organismo_fasta import OrganismoFasta


def ler_fasta(arquivo):
    objetos_organismo = []
    with open(arquivo, "r") as file:
        linhas = file.readlines()
        id_ = None
        nome = None
        sequencia = ""
        for linha in linhas:
            linha = linha.strip()
            if linha.startswith(">"):
                if id_ and nome and sequencia:
                    organismo = OrganismoFasta(id_, nome, sequencia)
                    objetos_organismo.append(organismo)
                id_ = linha[1:]
                nome = linha[1:].split()[0]
                sequencia = ""
            else:
                sequencia += linha
        if id_ and nome and sequencia:
            organismo = OrganismoFasta(id_, nome, sequencia)
            objetos_organismo.append(organismo)
    return objetos_organismo