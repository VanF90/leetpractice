class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Sort the list so that we can easily check for duplicates
        nums.sort()

        # Initialize a list to store the triplets
        triplets = []

        # Iterate through the list
        for i in range(len(nums)):
            # Make sure we aren't checking the same element twice by continuing
            # if we have already seen this element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Initialize pointers for the other two elements of the triplet
            left = i+1
            right = len(nums)-1

            # Find the other two elements of the triplet
            while left < right:
                # Check if the sum of the three elements is zero
                if nums[i] + nums[left] + nums[right] == 0:
                    # If it is, append the triplet to the list and move the pointers
                    triplets.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # Skip over any duplicate elements
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                # If the sum is too small, move the left pointer
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                # If the sum is too large, move the right pointer
                else:
                    right -= 1

        return triplets
