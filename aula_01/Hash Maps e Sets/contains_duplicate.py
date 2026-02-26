# ============================================================
# PROBLEMA:
# Dado um array de números, verifique se existe
# algum elemento duplicado.
#
# Exemplo:
# [1, 2, 3, 1] -> True
# [1, 2, 3, 4] -> False
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list, set
# ✔ Operadores -> in
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> set (HashSet)
# ✔ Funções -> def, return
# ============================================================

def contains_duplicate(numbers):
    seen = set()  # Estrutura HashSet (busca O(1))

    for num in numbers:  # Percorremos o array
        if num in seen:  # Verificamos se já vimos esse número
            return True  # Se já existe, é duplicado

        seen.add(num)  # Armazenamos no set

    return False


# Testando
array = [1, 2, 3, 1]
print("Array:", array)
print("Tem duplicado?", contains_duplicate(array))