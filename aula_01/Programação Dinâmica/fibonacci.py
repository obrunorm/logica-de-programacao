# ============================================================
# PROBLEMA:
# Dado um número n,
# retorne o n-ésimo número de Fibonacci.
#
# Exemplo:
# n = 6
#
# Sequência:
# 0, 1, 1, 2, 3, 5, 8
#
# Resultado: 8
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, list
# ✔ Estruturas de dados -> array (DP)
# ✔ Estruturas de controle -> for
# ✔ Programação Dinâmica -> reutilização de subproblemas
# ✔ Funções -> def, return
#
# IDEIA:
# Subproblema:
# fib(i) = fib(i-1) + fib(i-2)
#
# Transição:
# dp[i] = dp[i-1] + dp[i-2]
#
# Armazenamos resultados para evitar recomputação.
# ============================================================


def fibonacci(n):
    # Casos base
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Array para armazenar resultados
    dp = [0] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    # Preenche tabela
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ===== Testando =====
n = 6

print("n:", n)
print("Fibonacci:", fibonacci(n))