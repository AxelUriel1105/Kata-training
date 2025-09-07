"""Linked Lists - Length & Count

Implement length to count the number of nodes in a linked list.

length(null) => 0
length(1 -> 2 -> 3 -> null) => 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) => 0
count(1 -> 2 -> 3 -> null, 1) => 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) => 4
I've decided to bundle these two functions within the same Kata since they are both very similar.

The push()/Push() and buildOneTwoThree()/BuildOneTwoThree() functions do not need to be redefined."""
from preloaded import Node

# Node is defined in preloaded:
# class Node:
#     def __init__(self, data):
#        self.data = data
#        self.next = None

def length(node: Node) -> int:
    count = 0
    while node:
        count+=1
        node = node.next
    return count
def count(node: Node, data) -> int:
    count = 0
    while node:
        if data == node.data:
            count+=1
        node = node.next
    return count