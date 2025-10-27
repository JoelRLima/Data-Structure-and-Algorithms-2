# Atividade 1 – Comparação de Algoritmos de Dijkstra

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
