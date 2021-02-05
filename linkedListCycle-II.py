# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is not None:
            pt1 = head
        else: 
            return
        
        collect_list = [pt1]
                
        while pt1.next:
            pt1 = pt1.next
            if pt1 in collect_list:
                return pt1
            collect_list.append(pt1)        
            
        return         
        
        '''
        if pt1.next:
            pt2 = pt1.next
        else:
            return null
        
        while pt1 != pt2:
            if pt2.next is None or pt1.next is None: 
                return null
            elif pt2.next.next is None:
                return null
                pt1 = pt1.next
            else:
                pt2 = pt2.next.next
                pt1 = pt1.next
        
        return pt1
        
        '''
