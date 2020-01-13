
class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
     
def add_numbers(n1, n2):

    current1 = n1
    current2 = n2
        
    head = Node(0)
    currentHead = head
    
    sum = 0

    while current1 or current2:
        
        sum /= 10
        
        if current1 != None:
            sum += current1.val
            current1 = current1.next
        
        if current2 != None:
            sum += current2.val
            current2 = current2.next

        currentHead.next = Node(int(sum % 10))
        currentHead = currentHead.next
    
    if sum / 10 == 1:
        currentHead.next = Node(1)

    return head.next


def get_node(num):
    if len(num) == 0:
        return None
    tail = head = Node(num[0])
    for val in num[1:]:
        tmp = Node(val)
        tail.next = tmp
        tail = tail.next
    return head

def print_node(node):
    s = ''
    while node is not None:
        s += str(node.val)
        node = node.next
    print(''.join(reversed(s)))

n1 = Node(2)
n1.next = Node(4)

print_node(add_numbers(get_node([2, 4]), Node(7)))
print_node(add_numbers(get_node([2, 4]), get_node([2, 4])))
print_node(add_numbers(get_node([0, 2, 1]), get_node([0, 2, 1])))
print_node(add_numbers(get_node([9, 9]), Node(1)))
print_node(add_numbers(get_node([2, 4, 3]), get_node([5, 6, 4])))
print_node(add_numbers(get_node([0, 9, 9]), get_node([0, 1])))