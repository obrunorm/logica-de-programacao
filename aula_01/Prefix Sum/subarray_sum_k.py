# ============================================================
# PROBLEMA:
# Dado um array e um número K,
# retorne True se existir um subarray contínuo
# cuja soma seja igual a K.
#
# Exemplo:
# [1, 2, 3, 4], K = 6
# Resultado: True (1 + 2 + 3)
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list, dict
# ✔ Operadores -> +, -
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> HashMap (prefixos anteriores)
# ✔ Funções -> def, return
#
# IDEIA:
# Se soma_atual - K já apareceu antes,
# então existe subarray com soma K.
# ============================================================

def subarray_sum_k(numbers, k):
    prefix_sum = 0
    seen = {0: 1}  # Prefixo inicial

    for num in numbers:
        prefix_sum += num

        # Se já vimos prefix_sum - k antes,
        # existe subarray com soma K
        if prefix_sum - k in seen:
            return True

        # Armazena prefixo atual
        seen[prefix_sum] = 1

    return False


# ===== Testando =====
array = [1, 2, 3, 4]
k = 6

print("\nArray:", array)
print("K:", k)
print("Existe subarray com soma K?", subarray_sum_k(array, k))