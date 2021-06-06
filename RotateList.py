#https://leetcode.com/explore/learn/card/linked-list/213/conclusion/1295/
# According to Trial 36ms and 14.3mb
# 73.44% time and 59.89% space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        listNodes = []
        current = head
        while current != None:
            listNodes.append(current)
            current = current.next

        length = len(listNodes)

        k = k%length

        listNodes.reverse()

        part1 = listNodes[:k]
        part2 = listNodes[k:]

        part1.reverse()
        part2.reverse()


        part1.extend(part2)
        listNodes = part1

        rotatedList = listNodes[0]
        dummy = rotatedList

        for node in listNodes:
            dummy.next = node
            dummy = dummy.next

        dummy.next = None
        return rotatedList
