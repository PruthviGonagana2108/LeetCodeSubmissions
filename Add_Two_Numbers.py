# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        node1=[]
        node2=[]
        node1 = list_converter(l1)
        node2 = list_converter(l2)
        node1.reverse()
        node2.reverse()
        MainSum = list_addition(node1)+ list_addition(node2)
        non = number_to_linked_list(MainSum)
        mon = reverse_linked_list(non)
        return mon
        
def list_converter(x):
    current_node = x
    temp=[]
    while current_node:
            #print(current_node.val)
            m= current_node.val
            temp.append(m)
            #print(temp)
            current_node = current_node.next
    return temp

def list_addition(y):
    sum=0
    for i in y:
        sum = sum*10 + i
    return sum

def number_to_linked_list(num):
    # Edge case: if the number is 0
    if num == 0:
        return ListNode(0)

    # Create the head of the linked list
    head = None

    while num > 0:
        digit = num % 10  # Get the rightmost digit
        new_node = ListNode(digit)

        # Set the next of new node to the current head
        new_node.next = head

        # Update the head to the new node
        head = new_node

        num //= 10  # Remove the rightmost digit

    return head
def reverse_linked_list(head):
    previous_node = None
    current_node = head
    while current_node is not None:
        next_node = current_node.next  # Save the next node
        current_node.next = previous_node  # Reverse the link
        previous_node = current_node  # Move previous_node to current node
        current_node = next_node  # Move to the next node
    return previous_node  # New head of the reversed list
