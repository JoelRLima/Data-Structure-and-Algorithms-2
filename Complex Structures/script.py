# Gera o grafo no formato graphml

from operator import itemgetter
import networkx as nx
import wikipedia
import matplotlib.pyplot as plt
import re
from difflib import SequenceMatcher

SEEDS = [
    "Complex Network",       # Assunto original
    "Artificial Intelligence", # Assunto Tech
    "Climate change",        # Assunto Natureza/Ciência
    "Nelson Mandela",        # Assunto Histórico/Político
    "Earth"            # Assunto Cultura Pop
]
STOPS = ("International Standard Serial Number",
         "International Standard Book Number",
         "National Diet Library",
         "International Standard Name Identifier",
         "International Standard Book Number (Identifier)",
         "Pubmed Identifier",
         "Pubmed Central",
         "Digital Object Identifier",
         "Arxiv",
         "Proc Natl Acad Sci Usa",
         "Bibcode",
         "Library Of Congress Control Number",
         "Jstor",
         "Doi (Identifier)",
         "Isbn (Identifier)",
         "Pmid (Identifier)",
         "Arxiv (Identifier)",
         "Bibcode (Identifier)")

todo_lst = []    # A fila de processamento
todo_set = set() # Para evitar duplicatas na fila
done_set = set() # Para guardar o que já foi processado

for subject in SEEDS:
    # Formata o título para evitar erros (ex: minúsculas/maiúsculas)
    s_title = subject.title()

    # Adiciona na fila apenas se ainda não estiver lá
    if s_title not in todo_set:
        todo_lst.append((0, s_title)) # (camada, titulo)
        todo_set.add(s_title)

print(f"Começando a raspagem com {len(todo_lst)} tópicos iniciais: {todo_set}")

g = nx.DiGraph()
layer, page = todo_lst[0]

MAX_LINKS = 12
LIMIT_LAYER = 3

padrao_lixo = re.compile(r'(Categoria:|Lista de|Ficheiro:|Predefinição:|Wikipédia:|International Standard|\d{4})')

def calcular_relevancia(texto_base, candidato):
    try:
        score = SequenceMatcher(None, texto_base.lower(), candidato.lower()).ratio()
        if texto_base.lower() in candidato.lower() or candidato.lower() in texto_base.lower():
            score += 0.2
        return score
    except:
        return 0

while todo_lst:
    current_layer, page = todo_lst.pop(0)

    if current_layer >= LIMIT_LAYER:
        continue

    done_set.add(page)

    print(f"Camada: {current_layer} | Processando: {page}")

    try:
        wiki = wikipedia.page(page, auto_suggest=False)
    except Exception as e:
        print(f"  -> Erro ao carregar '{page}': {e}")
        continue

    # --- HEURÍSTICA HÍBRIDA ---

    todos_links = wiki.links
    candidatos_com_score = []
    candidatos_reserva = []

    for link in todos_links:
        if link in STOPS or padrao_lixo.search(link):
            continue
        if link in todo_set or link in done_set:
            continue

        score = calcular_relevancia(page, link)

        if score > 0.4:
            candidatos_com_score.append((link, score))
        else:
            candidatos_reserva.append(link)

    # Seleção
    candidatos_com_score.sort(key=lambda x: x[1], reverse=True)
    vip_links = [x[0] for x in candidatos_com_score]

    selecionados = vip_links[:MAX_LINKS]
    vagas_restantes = MAX_LINKS - len(selecionados)

    if vagas_restantes > 0:
        selecionados.extend(candidatos_reserva[:vagas_restantes])

    # Adicionar ao Grafo e à Fila
    for link_escolhido in selecionados:
        g.add_edge(page, link_escolhido)

        if link_escolhido not in todo_set:
            todo_lst.append((current_layer + 1, link_escolhido))
            todo_set.add(link_escolhido)

print("-" * 30)
print(f"Grafo finalizado: {len(g)} nós, {nx.number_of_edges(g)} arestas")

original = g.copy()

# remove self loops
g.remove_edges_from(nx.selfloop_edges(g))

# identify duplicates like that: 'network' and 'networks'
duplicates = [(node, node + "s")
              for node in g if node + "s" in g
             ]

for dup in duplicates:
  # *dup is a technique named 'unpacking'
  g = nx.contracted_nodes(g, *dup, self_loops=False)

print(duplicates)

duplicates = [(x, y) for x, y in
              [(node, node.replace("-", " ")) for node in g]
                if x != y and y in g]
print(duplicates)

for dup in duplicates:
  g = nx.contracted_nodes(g, *dup, self_loops=False)

# nx.contracted creates a new node/edge attribute called contraction
# the value of the attribute is a dictionary, but GraphML
# does not support dictionary attributes
nx.set_node_attributes(g, 0,"contraction")
nx.set_edge_attributes(g, 0,"contraction")

print("{} nodes, {} edges".format(len(g), nx.number_of_edges(g)))

# filter nodes with degree greater than or equal to 2
core = [node for node, deg in dict(g.degree()).items() if deg >= 2]

# select a subgraph with 'core' nodes
gsub = nx.subgraph(g, core)

print("{} nodes, {} edges".format(len(gsub), nx.number_of_edges(gsub)))

nx.write_graphml(gsub, "cna2.graphml")
