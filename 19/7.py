# class Node:
#     def __init__(self, item):
#         self.node = item
#         self.next = None
#         self.prev = None
#
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def get(self, value):
#         res = False
#         lnHead = self.head
#         lnTail = self.tail
#
#         while lnHead != lnTail:
#
#             if lnHead.node == value:
#                 res = lnHead.node
#                 return res
#
#             if lnTail.node == value:
#                 res = lnTail.node
#                 return res
#
#             lnHead = lnHead.next
#             lnTail = lnTail.prev
#         if lnHead.prev == lnTail: return res
#         return res
#
#     def dell(self, value):
#
#         lnHead = self.head
#         lnTail = self.tail
#
#         while lnHead != lnTail:
#
#             if lnHead.node == value:
#                 lnHead.next, lnHead.prev = lnHead.prev, lnHead.next
#                 return
#
#     if lnTail.node == value:
#         lnTail.prev.next = lnTail.next
#         lnTail.next.prev = lnTail.prev
#         return
#
#     lnHead = lnHead.next
#     lnTail = lnTail.prev
#
#     if lnHead.prev == lnTail: return
#         return
#
#
#     def addNode(self, item):
#         if not self.head:
#             self.head = Node(item)
#             return
#
#         lnList = self.tail if self.tail else self.head
#
#         self.tail = Node(item)
#         self.tail.next = self.head
#         self.tail.prev = lnList
#
#         lnList.next = self.tail
#         self.head.prev = self.tail
#
#         return
#
#
# t = DoubleLinkedList()
# for i in range(4, 10):
#     t.addNode(i)
# print(t.get(8))
# t.dell(7)
# print(t.get(7))
