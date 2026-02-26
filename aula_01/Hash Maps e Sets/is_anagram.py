# ============================================================
# PROBLEMA:
# Dadas duas strings, verifique se uma é anagrama da outra.
# Anagrama = mesmas letras com mesmas quantidades.
#
# Exemplo:
# "amor" e "roma" -> True
# "amor" e "ramo" -> True
# "amor" e "bola" -> False
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> string, dict
# ✔ Operadores -> ==, +=
# ✔ Estruturas de controle -> for, if
# ✔ Estruturas de dados -> dict (HashMap)
# ✔ Funções -> def, return
# ============================================================

def is_anagram(s1, s2):
    # Se tamanhos diferentes, não pode ser anagrama
    if len(s1) != len(s2):
        return False

    count = {}  # HashMap para contar letras

    # Contamos caracteres da primeira palavra
    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    # Subtraímos usando a segunda palavra
    for char in s2:
        if char not in count:
            return False

        count[char] -= 1

        if count[char] < 0:
            return False

    return True


# Testando
word1 = "amor"
word2 = "roma"

print("Palavra 1:", word1)
print("Palavra 2:", word2)
print("São anagramas?", is_anagram(word1, word2))