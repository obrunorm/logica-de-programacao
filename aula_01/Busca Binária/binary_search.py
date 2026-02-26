# ============================================================
# PROBLEMA:
# Dado um array ordenado e um número target,
# retorne o índice do elemento se ele existir.
# Caso contrário, retorne -1.
#
# Exemplo:
# [1, 3, 5, 7, 9], target = 5
# Resultado: 2
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Operadores -> <, >, ==, //
# ✔ Estruturas de controle -> while, if, elif
# ✔ Estruturas de dados -> array ordenado
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Calcular o meio
# 2. Comparar com target
# 3. Eliminar metade do array
# ============================================================

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid = (left + right) // 2  # Divisão inteira

        # Se encontramos o elemento
        if numbers[mid] == target:
            return mid

        # Se o valor do meio é menor que o target
        elif numbers[mid] < target:
            left = mid + 1  # Eliminamos a metade esquerda

        # Se o valor do meio é maior
        else:
            right = mid - 1  # Eliminamos a metade direita

    return -1  # Não encontrado


# ===== Testando =====
array = [1, 3, 5, 7, 9]
target = 5

print("Array:", array)
print("Target:", target)
print("Índice encontrado:", binary_search(array, target))