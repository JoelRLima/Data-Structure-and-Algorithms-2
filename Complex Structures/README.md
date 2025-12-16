## Análise de Redes Complexas na Wikipedia
Este projeto foi desenvolvido como Trabalho __Final da disciplina de Algoritmos e Estrutura de Dados II__. O objetivo é construir, visualizar e analisar uma rede complexa gerada a partir de artigos da Wikipedia, explorando as conexões semânticas entre diferentes tópicos.

> Link do vídeo: https://www.youtube.com/watch?v=eA3HfkdZ5gs

> Link da página web com o grafo: https://joelrlima.github.io/Data-Structure-and-Algorithms-2/Complex%20Structures/network/

### 👥 Autores
* Sueyvid

* Joel

* Ênio 

## 🎯 Objetivo
O notebook tem como objetivo construir uma rede direcionada onde:

* __Nós__: São páginas da Wikipedia.

* __Arestas__: São os hiperlinks (referências) de uma página para outra.

O projeto aplica conceitos de teoria dos grafos para analisar a topologia da rede, eliminar duplicatas e focar nos nós mais relevantes através de métricas de centralidade .

## 🧠 A Heurística de Construção (Snowballing)
Devido ao crescimento exponencial do grafo (Explosão Combinatória), a coleta de dados da __Camada 2 para a Camada 3__ utiliza uma Heurística Híbrida de Similaridade Semântica para filtrar os links mais relevantes.

Como funciona:

1. __Sementes (Seeds)__: O grafo inicia com tópicos centrais definidos manualmente (ex: Complex Network, Artificial Intelligence, Global Warming) .

1. __Filtragem (Blacklist)__: Remove links estruturais irrelevantes como datas, ISBN, identificadores de bibliotecas e categorias de manutenção .

1. __Heurística Centrípetra__:

    * Ao expandir um nó, o algoritmo calcula a __similaridade textual__ (usando ```difflib.SequenceMatcher```) entre o título da página atual e seus links.

    * Links com alta similaridade recebem prioridade (Score > 0.4).

1. __Estratégia Híbrida (Fallback):__

    * O algoritmo tenta preencher ```MAX_LINKS``` (ex: 10) com os melhores candidatos semânticos.

    * Caso não haja candidatos qualificados suficientes, ele completa as vagas restantes com outros links válidos da página para garantir a continuidade da expansão da rede.

## 🛠️ Tecnologias Utilizadas
O projeto foi desenvolvido em __Python 3__ utilizando as seguintes bibliotecas:

[__Wikipedia-API__](https://pypi.org/project/wikipedia/): Para crawling e obtenção dos links das páginas.

[__NetworkX__](https://networkx.org/): Para construção, manipulação e cálculo de métricas do grafo.

[__Matplotlib__](https://networkx.org/): Para plotagem de histogramas de grau e visualização de dados.

__Difflib & Re__: Bibliotecas padrão para processamento de texto e expressões regulares.

## 🚀 Como Executar
### Pré-requisitos
Instale as dependências listadas no notebook ou no requirements.txt:

```bash
pip install wikipedia networkx matplotlib
```

### Configuração
No início do notebook, você pode ajustar os parâmetros de controle da rede:

```python
MAX_LINKS = 10     # Número máximo de filhos por nó (Branching Factor)
LIMIT_LAYER = 3    # Profundidade máxima da rede (0 -> 1 -> 2 -> 3)
```

### Exportação dos Dados
Ao final da execução, o script gera histogramas da distribuição de graus dos nós  e exporta a rede final (ou o subgrafo principal) para o formato __GraphML__, que pode ser aberto no Gephi ou Cytoscape:

```Python
nx.write_graphml(gsub, "cna.graphml")
```

## 📊 Processamento de Dados
O pipeline de dados segue as etapas:

1. __Coleta__: Raspagem dos dados com a heurística aplicada.

1. __Limpeza__: Remoção de self-loops e fusão de nós duplicados (ex: "Network" e "Networks") .

1. __Poda (Truncate)__: Geração de um subgrafo contendo apenas o "Core" da rede (nós com grau >= 2) para melhor visualização .

_Este projeto é estritamente educacional e utiliza dados públicos da Wikipedia._



