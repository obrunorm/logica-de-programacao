# ============================================================
# PROBLEMA:
# Dado um array de números, retorne um dicionário
# com a frequência de cada número.
#
# Exemplo:
# [1, 2, 2, 3, 1, 1]
# Resultado -> {1: 3, 2: 2, 3: 1}
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list, dict
# ✔ Operadores -> +=
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> dict (HashMap)
# ✔ Funções -> def, return
# ============================================================

def count_frequency(numbers):
    frequency = {}  # HashMap

    for num in numbers:
        if num in frequency:
            frequency[num] += 1  # Atualiza contador
        else:
            frequency[num] = 1   # Primeira ocorrência

    return frequency


# Testando
array = [1, 2, 2, 3, 1, 1]

print("Array:", array)
print("Frequência:", count_frequency(array))