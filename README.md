# Algoritmo de Kruskal: rede de túneis em Marte

Implementação do **algoritmo de Kruskal** para encontrar a **Árvore Geradora Mínima (AGM / MST)** de um grafo, desenvolvida para a disciplina de Teoria dos Grafos.

## O problema

Uma colônia em Marte tem 6 bases (Habitat, Estufa, Mina, Usina, Lab e Porto) que precisam ser ligadas por túneis subterrâneos. Existem 10 túneis possíveis, cada um com um custo em metros de escavação. O programa calcula quais túneis escavar para **ligar todas as bases com o menor total de metros possível**.

| Problema | Grafo |
|---|---|
| Base | Vértice |
| Túnel | Aresta |
| Metros de escavação | Peso da aresta |

## Dependências

- **Python 3.6 ou superior**
- **Nenhuma biblioteca externa.** O código usa apenas recursos nativos do Python, e nada precisa ser instalado com `pip`.

Para conferir a versão do Python instalada:

```bash
python3 --version
```

## Como executar

1. Baixe o arquivo `kruskal_marte.py`.
2. Abra o terminal na pasta onde está o arquivo.
3. Execute:

```bash
python3 kruskal_marte.py
```

> No Windows, pode ser necessário usar `python kruskal_marte.py` ou `py kruskal_marte.py`.

## Saída esperada

```
=== PASSO A PASSO ===
Habitat - Estufa (120 m): ACEITO
Habitat - Lab (150 m): ACEITO
Estufa - Lab (180 m): REJEITADO (formaria ciclo)
Estufa - Mina (210 m): ACEITO
Mina - Lab (230 m): REJEITADO (formaria ciclo)
Usina - Porto (240 m): ACEITO
Habitat - Usina (260 m): ACEITO
Lab - Porto (300 m): REJEITADO (formaria ciclo)
Mina - Usina (340 m): REJEITADO (formaria ciclo)
Mina - Porto (410 m): REJEITADO (formaria ciclo)

=== TÚNEIS ESCOLHIDOS ===
Ligar Habitat a Estufa (120 m)
Ligar Habitat a Lab (150 m)
Ligar Estufa a Mina (210 m)
Ligar Usina a Porto (240 m)
Ligar Habitat a Usina (260 m)

Total mínimo: 980 metros de túnel
```

## Estrutura do código

O código está em um único arquivo e segue o pseudocódigo do livro *Algoritmos: Teoria e Prática* (Cormen et al.):

- **`make_set(v)`**: cria um conjunto isolado para o vértice `v`.
- **`find_set(v)`**: retorna o conjunto ao qual `v` pertence.
- **`union(u, v)`**: une os conjuntos de `u` e `v`.
- **`kruskal(vertices, arestas)`**: ordena as arestas por peso e aceita cada uma que não forme ciclo, ou seja, que ligue vértices de conjuntos diferentes.

**Complexidade:** O(E log E + V²), em que E é o número de arestas e V o número de vértices.

## Como testar com outro grafo

Basta alterar as listas `bases` e `tuneis` no final do arquivo. Cada túnel segue o formato `(vértice 1, vértice 2, peso)`.