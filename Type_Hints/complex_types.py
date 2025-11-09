'''
Python allows providing hints about more complex types: lists, tuples, dicts and sets.

The example below is based on leetcode's 1st problem: Two Sum
https://leetcode.com/problems/two-sum/description/
'''

class getTwoSum:
    def __init__(self, ):
        print(f"Created {self.__class__.__name__} class object")

    # Take a list of integers and an integer as inputs, output a list of integers.
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_2_idx: dict[int, int] = {}  # Dictionary with int-int key-value pairs.
        for i in range(len(nums)):
            if nums[i] not in num_2_idx:
                num_2_idx[nums[i]] = i
            if (target - nums[i]) in num_2_idx.keys() and num_2_idx[target - nums[i]] != i:
                return [i, num_2_idx[target - nums[i]]]
        return [-1, -1]

def main():
    g2s = getTwoSum()
    for input in [([2, 7, 11, 15], 9), ([3, 2, 4], 6), ([3, 3], 6)]:
        print(f"{input} -> {g2s.twoSum(input[0], input[1])}")

if __name__ == "__main__":
    main()