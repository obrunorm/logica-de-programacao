# ============================================================
# PROBLEMA:
# Dado um array onde todos os números aparecem duas vezes,
# exceto um que aparece apenas uma vez,
# retorne esse número único.
#
# Exemplo:
# [4, 1, 2, 1, 2]
#
# Resultado: 4
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Estruturas de dados -> array
# ✔ Estruturas de controle -> for
# ✔ Operadores binários -> XOR (^)
# ✔ Funções -> def, return
#
# IDEIA:
# XOR possui propriedades importantes:
# a ^ a = 0
# a ^ 0 = a
# XOR é comutativo e associativo
#
# Então:
# 4 ^ 1 ^ 2 ^ 1 ^ 2
# = (1 ^ 1) ^ (2 ^ 2) ^ 4
# = 0 ^ 0 ^ 4
# = 4
#
# Ou seja, todos os números duplicados se cancelam.
# ============================================================


def single_number(nums):
    result = 0

    for num in nums:
        result ^= num  # Aplica XOR acumulado

    return result


# ===== Testando =====
array = [4, 1, 2, 1, 2]

print("Array:", array)
print("Número único:", single_number(array))