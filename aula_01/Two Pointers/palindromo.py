# ============================================================
# PROBLEMA:
# Dada uma string, verifique se ela é um palíndromo.
# Um palíndromo é uma palavra que pode ser lida igual
# de frente para trás.
#
# Exemplo:
# "radar" -> True
# "python" -> False
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, string
# ✔ Operadores -> ==, !=, +=, -=, <
# ✔ Estruturas de controle -> while, if
# ✔ Estruturas de dados -> string (sequência indexada)
# ✔ Funções -> def, return
# ============================================================

def is_palindrome(text):
    # Criamos dois ponteiros (índices inteiros)
    left = 0                      # começa do início
    right = len(text) - 1         # começa do final
    palindromo = "é um palindromo"
    naoPalindromo = "não é um palindromo"

    # Enquanto os ponteiros não se cruzarem
    while left < right:

        # Comparamos os caracteres
        if text[left] != text[right]:
            return naoPalindromo  # Se forem diferentes, não é palíndromo

        # Movemos os ponteiros
        left += 1
        right -= 1

    # Se terminou o loop sem retornar False
    return palindromo


# Testando
word = "arara"
print("Palavra: ", word)
print(is_palindrome(word))