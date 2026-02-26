# ============================================================
# PROBLEMA:
# Dado um fluxo de números, calcule a mediana
# dinamicamente após cada inserção.
#
# Exemplo:
# Inserções: [1, 2, 3]
# Medianas: 1, 1.5, 2
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, float, list
# ✔ Operadores -> push/pop
# ✔ Estruturas de controle -> if
# ✔ Estruturas de dados -> Min Heap + Max Heap
# ✔ Funções -> métodos de inserção e cálculo
#
# IDEIA:
# 1. Manter duas heaps
# 2. Balancear tamanhos
# 3. Calcular mediana baseado no topo
# ============================================================

import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max Heap (negativos)
        self.large = []  # Min Heap

    def add_number(self, num):
        # Inserimos na Max Heap (invertendo sinal)
        heapq.heappush(self.small, -num)

        # Garantir que maior da small vá para large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balancear tamanhos
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def find_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2


# ===== Testando =====
mf = MedianFinder()

numbers = [1, 2, 3]

for num in numbers:
    mf.add_number(num)
    print(f"Inserido: {num}, Mediana atual: {mf.find_median()}")