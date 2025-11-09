'''
Python allows Optioal and Union types as part of typing module.

Union: indicates that a value can be one of multiple types.
Optional: indicates that a value may be None (Optional[type] == Union(type, None)).

The first example below is based on leetcode's 21st problem: Merge Two Sorted Lists.
https://leetcode.com/problems/merge-two-sorted-lists/description/
'''

from typing import Optional, Union

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeLinkedLists:
    @staticmethod   # Method that can be called without creating an object beforehand.
    def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:  # Both inputs as well as the output can be optionally taken/returned (linked lists can be null).
        if not list1 and not list2:
            return
        prev: ListNode = None
        cur: ListNode
        ret: ListNode
        while list1 or list2:
            if not list1:
                cur = list2
                list2 = list2.next
            elif not list2:
                cur = list1
                list1 = list1.next
            else:
                if list1.val > list2.val:
                    cur = list2
                    list2 = list2.next
                else:
                    cur = list1
                    list1 = list1.next
            if prev == None:
                ret = cur
                prev = cur
            else:
                prev.next = cur
            prev = cur
        return ret

def testLLMerger() -> None:
    node_1_3 = ListNode(4)
    node_1_2 = ListNode(2, node_1_3)
    node_1_1 = ListNode(1, node_1_2)
    head_1 = node_1_1

    node_2_3 = ListNode(4)
    node_2_2 = ListNode(3, node_2_3)
    node_2_1 = ListNode(1, node_2_2)
    head_2 = node_2_1

    # Linked lists can be null.
    def getListFromLL(node: Optional[ListNode]) -> list[int]:
        ret = []
        while node:
            ret.append(node.val)
            node = node.next
        return ret

    LL_as_list_1 = getListFromLL(head_1)
    LL_as_list_2 = getListFromLL(head_2)

    merged = MergeLinkedLists.mergeTwoLists(head_1, head_2)
    
    print(f"{LL_as_list_1} + {LL_as_list_2} = {getListFromLL(merged)}")

# Type of elements within provided list can be either float or int.
def binarySearch(nums: list[Union[int, float]], target: Union[int, float], l: int = 0, r: int = -1) -> int:
    if r == -1:
        r = len(nums) - 1

    if l > r:
        return -1

    m = l + (r - l) // 2

    if nums[m] == target:
        return m
    elif target < nums[m]:
        return binarySearch(nums, target, l, m - 1)
    else:
        return binarySearch(nums, target, m + 1, r)

def testBinarySearch() -> None:
    arr = [1, 3, 5, 7, 9]
    print(arr)
    for i in [5, 6, 1]:
        print(f"{i} -> {binarySearch(arr, i)}")

def main():
    testLLMerger()
    testBinarySearch()

if __name__ == "__main__":
    main()