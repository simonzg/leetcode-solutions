import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = [(l.val, i) for i, l in enumerate(lists) if l]
        heapq.heapify(heap)

        dummy = ListNode(0)
        cur = dummy

        while heap:
            val, i = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            L = lists[i]
            if L and L.next:
                lists[i] = L.next
                heapq.heappush(heap, (lists[i].val, i))
        return dummy.next
