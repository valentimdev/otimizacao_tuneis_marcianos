# Algoritmo de Kruskal - rede de túneis de uma colônia em Marte

# ---------- Operações de conjuntos (MAKE-SET, FIND-SET, UNION) ----------

conjunto = {}   # guarda em qual conjunto (ilha) cada vértice está


def make_set(v):
    # Cria um conjunto isolado para o vértice v
    conjunto[v] = v


def find_set(v):
    # Retorna o nome do conjunto ao qual v pertence
    return conjunto[v]


def union(u, v):
    antigo = conjunto[v]
    novo = conjunto[u]
    for x in conjunto: #Percorre todo mundo e troca onde era V por U
        if conjunto[x] == antigo:
            conjunto[x] = novo


# ---------- Algoritmo de Kruskal ----------

def kruskal(vertices, arestas):
    A = []                                      # Comeca a MST

    for v in vertices:                          
        make_set(v)                             

    arestas_ordenadas = sorted(arestas, key=lambda aresta: aresta[2])  # Ordena as arestas pelo peso

    for (u, v, peso) in arestas_ordenadas:    
        if find_set(u) != find_set(v):          
            A.append((u, v, peso))              
            union(u, v)                         
            print(f"{u} - {v} ({peso} m): ACEITO")
        else:
            print(f"{u} - {v} ({peso} m): REJEITADO (formaria ciclo)")

    return A                                  


# ---------- Problema em marte ----------

# As 6 bases da colônia (vértices)
bases = ["Habitat", "Estufa", "Mina", "Usina", "Lab", "Porto"]

# Túneis possíveis: (base 1, base 2, metros de túnel)
tuneis = [
    ("Habitat", "Estufa", 120),
    ("Habitat", "Lab", 150),
    ("Estufa", "Lab", 180),
    ("Estufa", "Mina", 210),
    ("Mina", "Lab", 230),
    ("Usina", "Porto", 240),
    ("Habitat", "Usina", 260),
    ("Lab", "Porto", 300),
    ("Mina", "Usina", 340),
    ("Mina", "Porto", 410),
]


print("=== PASSO A PASSO ===")
mst = kruskal(bases, tuneis)

print("\n=== TÚNEIS ESCOLHIDOS ===")
total = 0
for (u, v, peso) in mst:
    print(f"Ligar {u} a {v} ({peso} m)")
    total += peso

print(f"\nTotal mínimo: {total} metros de túnel")