# ============================================================
# PROBLEMA:
# Dado um array de números e um valor alvo (target),
# retorne True se existirem dois números cuja soma seja igual ao target.
#
# Exemplo:
# array = [4, 1, 5, 3, 2]
# target = 6
#
# Resultado: True (1 + 5 ou 4 + 2)
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Estruturas de dados -> array
# ✔ Estruturas de controle -> while, if
# ✔ Ordenação -> sort()
# ✔ Técnica -> Two Pointers
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Ordenar o array.
# 2. Usar dois ponteiros (início e fim).
# 3. Se soma for menor que target, move esquerda.
# 4. Se soma for maior que target, move direita.
# ============================================================


def has_two_sum(nums, target):
    # Ordena o array
    nums.sort()

    left = 0
    right = len(nums) - 1

    while left < right:
        current_sum = nums[left] + nums[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1  # Precisamos aumentar a soma
        else:
            right -= 1  # Precisamos diminuir a soma

    return False


# ===== Testando =====
array = [4, 1, 5, 3, 2]
target = 6

print("Array:", array)
print("Target:", target)
print("Existe par com soma target?",
      has_two_sum(array, target))