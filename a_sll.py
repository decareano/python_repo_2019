# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
            
    def addTwoNumbers( l1: ListNode, l2: ListNode) -> ListNode:
        if(l1!=None and l2!=None):
            carry =0;
            result = ListNode(0)
            walker =  result
            while(l1 or l2 or carry):
                sum =0
                num_1 =0
                num_2 =0
                if l1:
                    num_1 = l1.val
                    l1=l1.next
                if l2:
                    num_2 = l2.vak
                    l2 = l2.next
                    sum = num_1 + num_2 + carry 
                if sum>9:
                    carry =1
                    sum -=10
                else:
                    carry =0
                    walker.val = sum
                    if((l1 or l2 or carry) and (walker.next == None)):
                        walker.next = ListNode(0)
                        walker = walker.next
                return result
            return None



l1 = [3]
l2 = [8]
ab = Solution.addTwoNumbers(l1, l2)
print(ab)
