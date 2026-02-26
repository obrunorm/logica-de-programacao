# ============================================================
# PROBLEMA:
# Dada uma string contendo apenas os caracteres:
# '(', ')', '{', '}', '[' e ']'
# determine se os parênteses estão válidos.
#
# Uma string é válida se:
# - Toda abertura tem um fechamento correspondente
# - A ordem está correta
#
# Exemplo:
# "()[]{}" -> True
# "(]" -> False
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> list (usada como stack), string
# ✔ Operadores -> append (push), pop, ==
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> Stack (usando lista)
# ✔ Funções -> def, return
#
# IDEIA:
# 1. Empilhar símbolos de abertura
# 2. Ao encontrar fechamento, desempilhar
# 3. Validar correspondência
# ============================================================

def is_valid_parentheses(s):
    stack = []  # Nossa pilha (LIFO)

    # Mapeamento de fechamento -> abertura correspondente
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for char in s:
        # Se for abertura, empilha
        if char in "([{":
            stack.append(char)

        else:
            # Se pilha estiver vazia, não há abertura correspondente
            if not stack:
                return False

            top = stack.pop()  # Desempilha

            # Verifica se corresponde corretamente
            if top != mapping[char]:
                return False

    # Se pilha estiver vazia no final, está válido
    return len(stack) == 0


# ===== Testando =====
text = "()[]{}"
print("String:", text)
print("É válida?", is_valid_parentheses(text))