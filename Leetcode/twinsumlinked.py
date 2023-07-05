from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
        
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        if not head or not head.next:
            return 0

        node_head = head.val
        node_tail = head.last.val
        answer = node_head + node_tail
        return answer
    
    head = [4,1,3]
    print(pairSum(pairSum, head))
    
    # NOTE: Unfinished