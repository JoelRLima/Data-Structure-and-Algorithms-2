# Atividade 1 – Comparação de Algoritmos de Dijkstra

Componentes:
- Joel Rodrigues de Lima
- Sueyvid José Barbosa Paulo

## 🎯 Objetivo
O objetivo desta atividade é comparar o desempenho e a pegada de carbono de três implementações do algoritmo de Dijkstra:
- **Versão Clássica (O(V²))**
- **Versão com Min-Heap (O((V+E) log V))**
- **Implementação do NetworkX (referência)**

A análise considera tempo de execução e emissões de CO₂ em diferentes tamanhos de grafos.

---

## 🧩 Metodologia

1. **Geração de grafos**
   - Grafos aleatórios gerados com `networkx.gnp_random_graph`.
   - Garantida a **conectividade** via componente gigante.
   - Pesos inteiros positivos atribuídos aleatoriamente no intervalo [1, 10].

2. **Configuração experimental**
   - Tamanhos testados: 100, 500, 1.000, 5.000, 10.000, 15.000 (até o limite suportado pela máquina).
   - **15 repetições** por tamanho.
   - **5 fontes aleatórias** por repetição.
   - Métricas coletadas:
     - Tempo de execução (segundos).
     - Emissões de CO₂ (gramas), via [CodeCarbon](https://mlco2.github.io/codecarbon/).

3. **Validação de corretude**
   - Em grafos pequenos, os três algoritmos retornaram resultados idênticos, garantindo que as diferenças observadas são apenas de desempenho.

4. **Estatística**
   - Cálculo de **médias**, **desvios-padrão** e **intervalos de confiança (95%)**.
   - Gráficos com barras de erro e sombreamento de IC.

---

## ⚙️ Como reproduzir

### Dependências
- Python 3.10+
- Bibliotecas:
  ```bash
  pip install networkx numpy pandas matplotlib codecarbon scipy

---

## 📑 Resultados Numéricos – Dijkstra Clássico (O(V²))

| Tamanho (nós) | Tempo médio (s)       | CO₂ médio (g)         |
|---------------|-----------------------|-----------------------|
| 100           | 0.001 ± 0.000         | 0.000006 ± 0.000000   |
| 500           | 0.025 ± 0.002         | 0.000082 ± 0.000005   |
| 1000          | 0.101 ± 0.007         | 0.000325 ± 0.000021   |
| 5000          | 2.584 ± 0.117         | 0.008237 ± 0.000372   |
| 10000         | 10.013 ± 0.093        | 0.031493 ± 0.000884   |

## 🔍 Análise dos Resultados

Os gráficos mostram que tanto o tempo de execução quanto a pegada de carbono aumentam com o crescimento do tamanho dos grafos, o que é esperado, já que problemas maiores exigem mais processamento e energia.

A sequência de desempenho se mantém em todos os casos:
Clássico > NetworkX > Min-Heap, tanto para tempo quanto para pegada de carbono.

Essa diferença é explicada pela complexidade dos algoritmos:

- Versão Clássica: possui complexidade $O(V²+E)$, pois a seleção do próximo vértice com menor distância é feita de forma linear, percorrendo todos os vértices ainda não visitados a cada iteração. Esse método é simples, mas torna-se ineficiente para grafos grandes.

- Versão NetworkX: utiliza implementações otimizadas e estruturas de dados mais eficientes, o que melhora o desempenho, mas ainda com certa sobrecarga devido à abstração da biblioteca.

- Versão Min-Heap: apresenta a melhor performance, com complexidade $O((V+E)log⁡V)$, graças ao uso da fila de prioridade (heap), que permite obter o vértice mínimo em tempo logarítmico.

Como consequência, algoritmos mais eficientes não apenas reduzem o tempo de execução, mas também diminuem o consumo energético e a pegada de carbono, evidenciando uma correlação direta entre eficiência computacional e sustentabilidade ambiental.

## Link do Vídeo


https://www.youtube.com/watch?v=eRvPA6L72Ag
