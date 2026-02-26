# ============================================================
# PROBLEMA:
# Dada a cabeça de uma lista ligada,
# retorne o nó do meio.
#
# Exemplo:
# 1 -> 2 -> 3 -> 4 -> 5
# Resultado: 3
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> Classe Node
# ✔ Operadores -> atribuição (=)
# ✔ Estruturas de controle -> while
# ✔ Estruturas de dados -> Linked List
# ✔ Funções -> def, return
# ============================================================


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def find_middle(head):
    slow = head  # Anda 1 passo
    fast = head  # Anda 2 passos

    # Quando fast chegar no final,
    # slow estará no meio
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Função auxiliar para imprimir lista
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# ===== Testando =====

# Criando lista: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print("Lista:")
print_list(head)

middle = find_middle(head)
print("Valor do meio:", middle.value)