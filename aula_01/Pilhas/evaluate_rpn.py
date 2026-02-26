# ============================================================
# PROBLEMA:
# Dada uma expressão em notação pós-fixa (Reverse Polish Notation),
# calcule o resultado.
#
# Exemplo:
# ["2", "1", "+", "3", "*"] -> 9
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> list, int
# ✔ Operadores -> +, -, *, /
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> Stack
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Se número -> empilha
# 2. Se operador -> desempilha dois valores
# 3. Aplica operação e empilha resultado
# ============================================================

def evaluate_rpn(tokens):
    stack = []

    for token in tokens:
        # Se for operador
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(int(a / b))  # divisão inteira

        else:
            # Converte string para inteiro
            stack.append(int(token))

    # Resultado final
    return stack[0]


# ===== Testando =====
expression = ["2", "1", "+", "3", "*"]
print("\nExpressão:", expression)
print("Resultado:", evaluate_rpn(expression))