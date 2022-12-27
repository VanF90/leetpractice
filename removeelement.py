class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for v in nums[:]:
                if v == val:
                    nums.remove(v)
        return len(nums)

