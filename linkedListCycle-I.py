# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        
        
        pt1 = head
        if pt1 == None:
            return False
        else:
            pt2 = head.next
            
        if pt2 == None:
            return False
        
               
        while pt1 != pt2:
                          
            if pt1.next:  
                pt1 = pt1.next
                
                if pt2.next:
                    if pt2.next.next:
                        pt2 = pt2.next.next
                    else:
                        return False
                else:
                    return False
            else:
                return False
            
            
        return True
            
        
        
