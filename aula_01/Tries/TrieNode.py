# ============================================================
# PROBLEMA:
# Implemente uma estrutura Trie (árvore de prefixos)
# com as seguintes operações:
#
# - insert(word)  -> insere uma palavra
# - search(word)  -> retorna True se a palavra existir
# - startsWith(prefix) -> retorna True se existir palavra com esse prefixo
#
# Exemplo:
# trie.insert("casa")
# trie.search("casa")      -> True
# trie.search("cas")       -> False
# trie.startsWith("cas")   -> True
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> str, bool
# ✔ Estruturas de dados -> dict (filhos), classe (TrieNode)
# ✔ Estruturas de controle -> for, if
# ✔ Funções -> def, return
#
# IDEIA:
# Percorremos letra por letra.
# Se o nó não existir, criamos.
# No final da palavra, marcamos como fim de palavra.
# ============================================================


# Nó da Trie
class TrieNode:
    def __init__(self):
        self.children = {}      # dicionário de filhos
        self.is_end = False     # marca fim da palavra


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Inserir palavra
    def insert(self, word):
        node = self.root

        for char in word:
            # Se a letra ainda não existir, cria
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        # Marca fim da palavra
        node.is_end = True

    # Buscar palavra completa
    def search(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end

    # Buscar prefixo
    def startsWith(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]

        return True


# ===== Testando =====
trie = Trie()

trie.insert("casa")
trie.insert("carro")

print("Buscar 'casa':", trie.search("casa"))
print("Buscar 'cas':", trie.search("cas"))
print("Prefixo 'cas':", trie.startsWith("cas"))
print("Prefixo 'ca':", trie.startsWith("ca"))
print("Prefixo 'z':", trie.startsWith("z"))