class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_ = { nums[i] : i for i in range(len(nums)) }

        for i in range(len(nums)):
            if dict_.has_key( target - nums[i] ) and i != dict_[target-nums[i]]:
                return [i, dict_[target - nums[i]]];


def main():
    solution = Solution()
    print solution.twoSum([3,2,4], 6)

main();
