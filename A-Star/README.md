# Trabalho 2 (Unidade 2): A* + MST para Conexão de POIs

**Autores:** Joel e Sueyvid

Link do Vídeo: [Vídeo do T2U2 - AED2 (Joel e Sueyvid)](https://www.youtube.com/watch?v=cw63i2my-L0)

Este repositório contém a implementação do Trabalho 2 da Unidade 2, que foca na aplicação dos algoritmos A* e MST (Árvore Geradora Mínima) para resolver um problema de otimização de rede em grafos viários.

## 🎯 Objetivo

O objetivo deste trabalho foi estimar a quilometragem mínima de **vias reais** necessária para interligar um conjunto de Pontos de Interesse (POIs) em 9 capitais do Nordeste brasileiro.

Seguindo os requisitos da tarefa, o POI escolhido para este projeto foi `{'tourism': 'museum'}` (museus), por ser diferente do notebook-base ('hospitais') e possuir um volume de dados gerenciável, o que se provou crucial para a análise de tempo de execução.

## ⚙️ Metodologia Aplicada

O nosso script (`atividadeunid2joel_e_sueyvid.py`) implementa um pipeline de 4 etapas para cada cidade:

1.  **Modelagem (OSMnx):** O grafo viário de cada cidade é baixado usando `OSMnx`. O passo crítico é a projeção do grafo para o sistema UTM (`ox.project_graph`), que nos permite calcular distâncias reais em metros.

2.  **Cálculo de Rotas (A*):** Foi calculado o caminho mais curto entre *todos os pares* de museus. Para isso, usámos o algoritmo **A*** (`nx.astar_path` e `nx.astar_path_length`). A heurística utilizada foi a `heuristic_great_circle`, que calcula a distância do "círculo máximo" considerando a curvatura da Terra. Todas as rotas (listas de nós) e os seus custos (km) foram armazenados.

3.  **Otimização (MST):** Um novo **grafo completo** simples (`G_interest`) foi construído. Neste grafo, os nós são *apenas* os museus e o peso de cada aresta é a distância A* (em km) calculada na etapa anterior. Sobre este grafo, aplicámos o algoritmo de **Árvore Geradora Mínima (MST)** para encontrar a rede de conexão total com o menor custo em km.

4.  **Reconstrução e Visualização:** As arestas da MST (ex: "Museu A" -> "Museu B") foram "mapeadas de volta" para as rotas de rua reais que tínhamos armazenado. O resultado final é uma plotagem da união de todas essas rotas, sobrepostas ao mapa da cidade.

## 🛠️ Tecnologias Utilizadas

* **OSMnx:** Para download e modelagem dos grafos viários do OpenStreetMap.
* **NetworkX:** Para a manipulação dos grafos e execução dos algoritmos A* e MST.
* **Pandas:** Para a estruturação e apresentação da tabela comparativa final.
* **Matplotlib:** Para a visualização dos grafos e das rotas.

## 🚀 Como Executar o Projeto

1.  Clone este repositório.
2.  Instale as dependências necessárias:
    ```bash
    pip install osmnx networkx pandas matplotlib
    ```
3.  Execute o script principal:
    ```bash
    python atividadeunid2joel_e_sueyvid.py
    ```
4.  O script irá processar todas as 9 cidades, imprimir a tabela de resultados no console e, em seguida, exibir os 9 gráficos de mapa sequencialmente.

## 📊 Resultados: Tabela Comparativa

A tabela abaixo (gerada pelo script) consolida as métricas de rede para os POIs (museus) nas 9 capitais do Nordeste.

| Cidade     | Nós de POI | Comprimento MST (km) | Média km/POI | Média km/Aresta |
|            |            |                      |              |                 |
| Natal      | 13         | 19.63                | 1.51         | 1.64            |
| Fortaleza  | 18         | 37.28                | 2.07         | 2.19            |
| Salvador   | 36         | 41.24                | 1.15         | 1.18            |
| Recife     | 27         | 26.75                | 0.99         | 1.03            |
| São Luís   | 19         | 27.40                | 1.44         | 1.52            |
| Maceió     | 10         | 6.09                 | 0.61         | 0.68            |
| João Pessoa| 11         | 27.66                |  2.51        | 2.77            |
| Teresina   | 8          | 12.28                | 1.54         | 1.75            |
| Aracaju    | 5          | 8.08                 | 1.62         | 2.02            |

---

## 🔬 Análise Crítica (Requisito 6)

A análise da tabela de resultados e dos logs de processamento revela pontos cruciais sobre o método.

Primeiro, a quilometragem da MST é altamente influenciada pela **dispersão geográfica** dos POIs, um fator que o nosso modelo capturou bem. Isto é evidente ao comparar **Maceió** e **João Pessoa**: ambas têm um número similar de museus (10 e 11, respetivamente), mas resultados drasticamente diferentes. Maceió exigiu apenas 6.09 km de rede (com a menor média, 0.61 km/POI), sugerindo que os seus museus são altamente clusterizados. Em contraste, João Pessoa exigiu 27.66 km (com a maior média, 2.51 km/POI), indicando que os seus museus são geograficamente muito dispersos.

Segundo, a **limitação computacional** do método foi comprovada pelos nossos tempos de execução. O cálculo das rotas A* entre todos os pares de POIs tem um **custo quadrático ($\text{N}^2$)**. Notavelmente, o tempo não depende apenas do *número* de POIs (N), mas da complexidade do grafo. A prova disso é a anomalia encontrada em **João Pessoa**: com N=11, o processamento levou **210 segundos**. Em comparação, **Salvador**, com N=36 (mais que o triplo de POIs), levou apenas **86 segundos**. Isto sugere que as rotas em João Pessoa são longas e complexas, exigindo mais esforço computacional do A* do que as rotas (provavelmente mais curtas) em Salvador. Isto prova que, se tivéssemos escolhido POIs com N=500+, o tempo de execução seria completamente inviável.


Finalmente, a qualidade dos nossos resultados é 100% dependente da **qualidade dos dados do OpenStreetMap**. POIs mal catalogados (ex: um museu em falta ou em local errado) ou ruas não mapeadas podem alterar significativamente o resultado final da MST.
