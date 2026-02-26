# ============================================================
# PROBLEMA:
# Dada uma lista ligada, verifique se existe um ciclo.
# Um ciclo ocorre quando um nó aponta para um nó anterior.
#
# Exemplo:
# 1 -> 2 -> 3 -> 4
#           ^     |
#           |_____|
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> Classe Node
# ✔ Operadores -> comparação (==)
# ✔ Estruturas de controle -> while
# ✔ Estruturas de dados -> Linked List
# ✔ Funções -> def, return
# ============================================================


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def has_cycle(head):
    slow = head  # Ponteiro lento (1 passo)
    fast = head  # Ponteiro rápido (2 passos)

    while fast and fast.next:
        slow = slow.next          # Avança 1 passo
        fast = fast.next.next     # Avança 2 passos

        if slow == fast:          # Se se encontrarem, há ciclo
            return True

    return False


# ===== Testando =====

# Criando lista com ciclo
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

head.next = second
second.next = third
third.next = fourth
fourth.next = second  # Criando ciclo

print("Existe ciclo?", has_cycle(head))