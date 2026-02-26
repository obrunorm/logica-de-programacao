# ============================================================
# PROBLEMA:
# Dado um array ordenado e um número alvo (target),
# retorne os índices de dois números cuja soma seja
# igual ao target.
#
# Exemplo:
# [1, 2, 4, 6, 10]
# target = 8
# Resultado -> (1, 3) pois 2 + 6 = 8
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Operadores -> +, ==, <, >
# ✔ Estruturas de controle -> while, if, elif
# ✔ Estruturas de dados -> lista (array)
# ✔ Funções -> def, return
# ============================================================

def two_sum_sorted(numbers, target):
    # Dois ponteiros
    left = 0
    right = len(numbers) - 1

    # Enquanto não se cruzarem
    while left < right:

        # Calculamos a soma atual
        current_sum = numbers[left] + numbers[right]

        # Se encontramos o alvo
        if current_sum == target:
            return left, right

        # Se a soma é menor que o alvo
        elif current_sum < target:
            left += 1  # aumentamos a soma movendo o ponteiro esquerdo

        # Se a soma é maior que o alvo
        else:
            right -= 1  # diminuímos a soma movendo o ponteiro direito

    return None


# Testando
array = [1, 2, 4, 6, 10]
target = 8

print("Array:", array)
print("Target:", target)
print("Resultado:", two_sum_sorted(array, target))