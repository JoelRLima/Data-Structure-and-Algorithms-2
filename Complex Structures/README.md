## Como executar o projeto

Este projeto foi desenvolvido em formato de **notebook Jupyter**. A forma recomendada de execução é executar todas as células em sequência, do início ao fim.

### Passo a passo

1. Abra o notebook do projeto (`.ipynb`) no Jupyter Notebook ou no Google Colab.
2. Certifique-se de que todas as dependências utilizadas no notebook estejam instaladas.
3. Execute o notebook utilizando a opção **Run all** (*Executar tudo*), ou, alternativamente, execute as células **uma a uma, em ordem**, de cima para baixo.

> **Importante:** não pule células, pois o código depende de variáveis e estruturas criadas nas etapas anteriores.

### Arquivo gerado

Ao final da execução, será gerado o arquivo: 

cna.graphml


Esse arquivo contém a estrutura completa da rede (vértices, arestas e atributos calculados) e é o artefato final do projeto.

### Uso no Gephi

1. Abra o software **Gephi**.
2. Importe o arquivo `cna.graphml`.
3. A partir desse arquivo, realize os cálculos de métricas, a aplicação de layouts e a geração das visualizações exigidas no trabalho.

### Observações

O notebook não requer parâmetros de entrada externos. Todas as etapas de coleta, construção da rede e exportação do grafo são executadas automaticamente durante a execução do código.
