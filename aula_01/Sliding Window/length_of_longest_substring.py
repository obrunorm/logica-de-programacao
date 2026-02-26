# ============================================================
# PROBLEMA:
# Dada uma string, encontre o tamanho da maior substring
# sem caracteres repetidos.
#
# Exemplo:
# "abcabcbb"
# Resultado: 3  (substring "abc")
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, string, set
# ✔ Operadores -> in, not in, +=, -
# ✔ Estruturas de controle -> for, while, if
# ✔ Estruturas de dados -> set (controle da janela)
# ✔ Funções -> def, return
#
# IDEIA DO SLIDING WINDOW:
# 1. Expandimos a janela com o ponteiro right
# 2. Se ficar inválida (caractere repetido), contraímos com left
# 3. Atualizamos o tamanho máximo
# ============================================================

def length_of_longest_substring(s):
    seen = set()   # Guarda caracteres atuais da janela
    left = 0       # Início da janela
    max_length = 0

    for right in range(len(s)):  # Expansão da janela
        while s[right] in seen:  # Se inválido (repetido)
            seen.remove(s[left]) # Contraímos removendo da esquerda
            left += 1

        seen.add(s[right])  # Adiciona novo caractere
        max_length = max(max_length, right - left + 1)

    return max_length


# ===== Testando =====
text = "abcabcbb"
print("String:", text)
print("Maior substring sem repetir:", length_of_longest_substring(text))