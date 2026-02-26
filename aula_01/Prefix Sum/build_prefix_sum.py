# ============================================================
# PROBLEMA:
# Dado um array de números, responda consultas de soma
# entre índices L e R (inclusive).
#
# Exemplo:
# Array: [2, 4, 6, 8]
# Soma de 1 até 3 -> 4 + 6 + 8 = 18
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Operadores -> +, -
# ✔ Estruturas de controle -> for
# ✔ Estruturas de dados -> array auxiliar (prefix)
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Criar array prefix
# 2. prefix[i] guarda soma até i
# 3. Soma(L, R) = prefix[R] - prefix[L-1]
# ============================================================

def build_prefix_sum(numbers):
    prefix = [0] * len(numbers)
    prefix[0] = numbers[0]

    for i in range(1, len(numbers)):
        prefix[i] = prefix[i - 1] + numbers[i]

    return prefix


def range_sum(prefix, left, right):
    if left == 0:
        return prefix[right]
    return prefix[right] - prefix[left - 1]


# ===== Testando =====
array = [2, 4, 6, 8]

prefix = build_prefix_sum(array)

print("Array:", array)
print("Prefix Sum:", prefix)
print("Soma do índice 1 ao 3:", range_sum(prefix, 1, 3))