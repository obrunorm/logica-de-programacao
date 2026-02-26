# ============================================================
# PROBLEMA:
# Dado um array ordenado, retorne o índice do primeiro
# elemento maior ou igual a X.
#
# Exemplo:
# [1, 3, 5, 7, 9], X = 6
# Resultado: 3 (valor 7)
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Operadores -> <, >=, //
# ✔ Estruturas de controle -> while
# ✔ Estruturas de dados -> array ordenado
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Sempre que encontrar valor >= X,
#    guarda possível resposta
# 2. Continua buscando à esquerda
# ============================================================

def lower_bound(numbers, target):
    left = 0
    right = len(numbers) - 1
    answer = -1  # Guarda melhor candidato

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] >= target:
            answer = mid      # Pode ser resposta
            right = mid - 1   # Continua procurando à esquerda
        else:
            left = mid + 1    # Procura à direita

    return answer


# ===== Testando =====
array = [1, 3, 5, 7, 9]
target = 6

print("\nArray:", array)
print("Target:", target)
print("Primeiro valor >= X está no índice:", lower_bound(array, target))