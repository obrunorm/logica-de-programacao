# ============================================================
# PROBLEMA:
# Dada uma árvore binária,
# retorne a altura (profundidade máxima) da árvore.
#
# Exemplo:
#        1
#       / \
#      2   3
#     /
#    4
#
# Resultado: 3
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> int, None
# ✔ Estruturas de dados -> TreeNode (estrutura hierárquica)
# ✔ Estruturas de controle -> if
# ✔ Recursão -> DFS (Depth First Search)
# ✔ Funções -> def, return
#
# IDEIA:
# A altura de um nó é:
# 1 + max(altura da esquerda, altura da direita)
#
# Percorremos a árvore usando DFS
# e combinamos os resultados dos filhos.
# ============================================================


# Definição da estrutura da árvore
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
    # Caso base: árvore vazia
    if root is None:
        return 0

    # Calcula altura da esquerda
    left_height = max_depth(root.left)

    # Calcula altura da direita
    right_height = max_depth(root.right)

    # Combina resultados
    return 1 + max(left_height, right_height)


# ===== Criando árvore para teste =====
#        1
#       / \
#      2   3
#     /
#    4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)


# ===== Testando =====
print("Altura da árvore:", max_depth(root))