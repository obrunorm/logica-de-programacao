# ============================================================
# PROBLEMA:
# Dado um conjunto de intervalos (início, fim),
# retorne o número máximo de intervalos
# que podem ser selecionados sem sobreposição.
#
# Exemplo:
# [(1,3), (2,4), (3,5), (6,8)]
#
# Resultado: 3
# (1,3), (3,5), (6,8)
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list, tuple
# ✔ Estruturas de dados -> lista de intervalos
# ✔ Estruturas de controle -> for, if
# ✔ Ordenação -> sorted()
# ✔ Estratégia -> Greedy
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Ordenar os intervalos pelo horário de término.
# 2. Sempre escolher o intervalo que termina primeiro.
# 3. Se o próximo não sobrepor, seleciona.
# ============================================================


def max_non_overlapping_intervals(intervals):
    # Ordena pelo fim do intervalo
    intervals.sort(key=lambda x: x[1])

    count = 0
    last_end = float('-inf')

    for start, end in intervals:
        # Se não sobrepõe
        if start >= last_end:
            count += 1
            last_end = end  # Atualiza fim do último escolhido

    return count


# ===== Testando =====
intervals = [(1, 3), (2, 4), (3, 5), (6, 8)]

print("Intervalos:", intervals)
print("Máximo sem sobreposição:",
      max_non_overlapping_intervals(intervals))