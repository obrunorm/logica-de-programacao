# ============================================================
# PROBLEMA:
# Dado um array de números distintos,
# retorne todas as permutações possíveis.
#
# Exemplo:
# Entrada: [1, 2, 3]
#
# Saída:
# [
#  [1, 2, 3],
#  [1, 3, 2],
#  [2, 1, 3],
#  [2, 3, 1],
#  [3, 1, 2],
#  [3, 2, 1]
# ]
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Estruturas de dados -> lista temporária
# ✔ Estruturas de controle -> for, if
# ✔ Recursão -> Backtracking
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Escolher um número que ainda não foi usado
# 2. Adicionar na lista temporária
# 3. Explorar recursivamente
# 4. Remover o número (desfazer escolha)
# ============================================================


def permute(nums):
    result = []
    path = []              # Lista temporária (estado atual)
    used = [False] * len(nums)  # Controle de elementos já usados

    def backtrack():
        # Se a permutação estiver completa
        if len(path) == len(nums):
            result.append(path[:])  # Copia a lista
            return

        for i in range(len(nums)):
            # Se já foi usado, pula
            if used[i]:
                continue

            # Escolhe
            used[i] = True
            path.append(nums[i])

            # Explora
            backtrack()

            # Desfaz escolha (Backtrack)
            path.pop()
            used[i] = False

    backtrack()
    return result


# ===== Testando =====
array = [1, 2, 3]

print("Array:", array)
print("Permutações:")
for p in permute(array):
    print(p)