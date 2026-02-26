# ============================================================
# PROBLEMA:
# Dada uma lista de intervalos [inicio, fim],
# mescle todos os intervalos que se sobrepõem.
#
# Exemplo:
# [[1,3],[2,6],[8,10],[15,18]]
# Resultado:
# [[1,6],[8,10],[15,18]]
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> list
# ✔ Operadores -> comparação (<, <=)
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> lista de pares
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Ordenar por início
# 2. Comparar com último intervalo inserido
# 3. Mesclar se houver sobreposição
# ============================================================

def merge_intervals(intervals):
    if not intervals:
        return []

    # Ordena pelo início
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]  # Começa com primeiro intervalo

    for current in intervals[1:]:
        last = merged[-1]

        # Se há sobreposição
        if current[0] <= last[1]:
            # Atualiza o fim para o maior valor
            last[1] = max(last[1], current[1])
        else:
            # Se não sobrepõe, adiciona novo intervalo
            merged.append(current)

    return merged


# ===== Testando =====
intervals = [[1,3],[2,6],[8,10],[15,18]]

print("Intervalos originais:", intervals)
print("Intervalos mesclados:", merge_intervals(intervals))