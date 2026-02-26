# ============================================================
# PROBLEMA:
# Dada uma lista de intervalos de reuniões,
# determine se existe algum conflito (sobreposição).
#
# Exemplo:
# [[1,3],[4,5],[2,6]] -> True (1-3 conflita com 2-6)
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> list
# ✔ Operadores -> comparação (<)
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> lista de pares
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Ordenar por início
# 2. Verificar se início atual < fim anterior
# ============================================================

def has_conflict(intervals):
    if not intervals:
        return False

    # Ordena por início
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):
        prev_end = intervals[i - 1][1]
        current_start = intervals[i][0]

        # Se o início atual for menor que o fim anterior, há conflito
        if current_start < prev_end:
            return True

    return False


# ===== Testando =====
meetings = [[1,3],[4,5],[2,6]]

print("\nReuniões:", meetings)
print("Existe conflito?", has_conflict(meetings))