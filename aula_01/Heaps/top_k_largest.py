# ============================================================
# PROBLEMA:
# Dado um array de números, retorne os K maiores elementos.
#
# Exemplo:
# [3, 2, 1, 5, 6, 4], k = 2
# Resultado: [5, 6]
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Operadores -> push/pop (heapq.heappush, heapq.heappop)
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> Heap (Priority Queue)
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Criar Min Heap
# 2. Inserir elementos
# 3. Se tamanho > k, remover menor
# 4. No final, heap contém os K maiores
# ============================================================

import heapq

def top_k_largest(numbers, k):
    min_heap = []  # Min Heap

    for num in numbers:
        heapq.heappush(min_heap, num)  # Insere elemento

        # Se heap ultrapassar tamanho K, remove o menor
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap


# ===== Testando =====
array = [3, 2, 1, 5, 6, 4]
k = 2

print("Array:", array)
print("Top K maiores:", top_k_largest(array, k))