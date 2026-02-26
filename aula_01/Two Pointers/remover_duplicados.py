# ============================================================
# PROBLEMA:
# Dado um array ordenado, remova os elementos duplicados
# "in-place" e retorne o novo tamanho.
#
# Exemplo:
# [1, 1, 2, 2, 3, 4, 4]
# Resultado -> [1, 2, 3, 4]
# Novo tamanho -> 4
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Operadores -> !=, +=
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> lista (array)
# ✔ Funções -> def, return
# ============================================================

def remove_duplicates(numbers):

    # Caso lista esteja vazia
    if not numbers:
        return 0

    # Ponteiro lento
    slow = 0

    # Ponteiro rápido percorre o array
    for fast in range(1, len(numbers)):

        # Se encontrar valor diferente
        if numbers[fast] != numbers[slow]:
            slow += 1
            numbers[slow] = numbers[fast]

    # Novo tamanho é slow + 1
    return slow + 1


# Testando
array = [1, 1, 2, 2, 3, 4, 4]

print("Array original:", array)

new_length = remove_duplicates(array)

print("Novo tamanho:", new_length)
print("Array sem duplicados:", array[:new_length])