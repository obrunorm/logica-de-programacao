# ============================================================
# PROBLEMA:
# Dado dois números inteiros a e b,
# retorne o Máximo Divisor Comum (MDC).
#
# Exemplo:
# a = 48
# b = 18
#
# Resultado: 6
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int
# ✔ Operadores -> %, =
# ✔ Estruturas de controle -> while
# ✔ Algoritmo matemático -> Algoritmo de Euclides
# ✔ Funções -> def, return
#
# IDEIA:
# Propriedade matemática:
# MDC(a, b) = MDC(b, a % b)
#
# Repetimos até que b seja 0.
# Quando b == 0, o resultado é a.
# ============================================================


def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Troca e aplica módulo
    return a


# ===== Testando =====
a = 48
b = 18

print("a:", a)
print("b:", b)
print("MDC:", gcd(a, b))