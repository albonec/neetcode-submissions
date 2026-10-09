# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = defaultdict(int)
        index = 0
        while head is not None:
            if head not in visited:
                visited[head] = index
                index += 1
                head = head.next
            else:
                return True
        return False

                

            
        