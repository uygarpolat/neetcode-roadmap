from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return [[]]

def main():
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    result = solution.threeSum(nums)
    assert(result == [[-1,-1,2],[-1,0,1]])
    
if __name__ == "__main__":
    main()