# ============================================================
# PROBLEMA:
# Dada a cabeça (head) de uma lista ligada,
# inverta a lista e retorne o novo head.
#
# Exemplo:
# 1 -> 2 -> 3 -> None
# Resultado:
# 3 -> 2 -> 1 -> None
#
# FUNDAMENTOS UTILIZADOS:
# ✔ Tipos de dados -> Classe Node
# ✔ Operadores -> atribuição (=)
# ✔ Estruturas de controle -> while
# ✔ Estruturas de dados -> Linked List
# ✔ Funções -> def, return
# ============================================================


# Definição do nó (estrutura base)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Ponteiro para o próximo nó


def reverse_linked_list(head):
    prev = None           # Nó anterior começa como None
    current = head        # Começamos do início da lista

    while current:
        next_node = current.next  # Guardamos o próximo nó
        current.next = prev       # Invertendo o ponteiro
        prev = current            # Avançamos prev
        current = next_node       # Avançamos current

    return prev  # Novo head


# Função auxiliar para imprimir a lista
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# ===== Testando =====

# Criando lista manualmente: 1 -> 2 -> 3
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print("Lista original:")
print_list(head)

reversed_head = reverse_linked_list(head)

print("Lista invertida:")
print_list(reversed_head)