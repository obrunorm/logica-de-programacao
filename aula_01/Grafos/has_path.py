# ============================================================
# PROBLEMA:
# Dado um grafo representado por lista de adjacência
# e dois nós (origem e destino),
# retorne True se existir caminho entre eles.
#
# Exemplo:
# grafo = {
#   0: [1, 2],
#   1: [2],
#   2: [3],
#   3: []
# }
#
# origem = 0
# destino = 3
#
# Resultado: True
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, bool
# ✔ Estruturas de dados -> dict (lista de adjacência), set (visitados)
# ✔ Estruturas de controle -> while, if
# ✔ Estrutura auxiliar -> fila (BFS)
# ✔ Funções -> def, return
#
# IDEIA:
# Usaremos BFS.
# Começamos da origem.
# Visitamos vizinhos.
# Marcamos como visitado para evitar ciclos.
# Se encontrarmos o destino, retornamos True.
# ============================================================

from collections import deque

def has_path(graph, start, end):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        # Se encontramos o destino
        if node == end:
            return True

        if node not in visited:
            visited.add(node)

            # Adiciona vizinhos na fila
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return False


# ===== Testando =====
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: []
}

start = 0
end = 3

print("Existe caminho?", has_path(graph, start, end))