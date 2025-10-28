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

## 🔍 Análise dos Resultados

Os gráficos mostram que, conforme o tamanho do grafo aumenta, tanto o tempo de execução quanto a pegada de carbono crescem. Esse comportamento é esperado, já que grafos maiores exigem mais operações computacionais e, consequentemente, maior consumo energético.

Em todas as medições, observa-se uma tendência consistente na ordem de desempenho dos métodos:

- Implementação Clássica (Clássico) apresenta os maiores valores de tempo e pegada de carbono;

- NetworkX aparece em posição intermediária;

- Min-Heap apresenta os melhores resultados, com menor tempo de execução e menor impacto ambiental.

Essa hierarquia indica que o uso de estruturas de dados mais eficientes, como a Min-Heap, reduz significativamente o custo computacional, o que, por consequência, diminui a energia consumida e a pegada de carbono. Já a versão clássica, possivelmente baseada em buscas lineares para encontrar o próximo vértice de menor distância, tem complexidade maior e, portanto, pior desempenho.

Além disso, a correlação entre tempo de execução e pegada de carbono é evidente: métodos mais rápidos tendem a consumir menos energia, confirmando que eficiência algorítmica contribui diretamente para sustentabilidade computacional.