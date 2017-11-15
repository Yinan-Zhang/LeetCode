class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [nums[0]];
        i = 0
        for num in nums:
            if i == 0:
                i+=1;
                continue;
            left.append(num*left[-1]);
            i += 1;

        print left

        right = [nums[-1]];
        i = 0
        for num in nums[::-1]:
            if i == 0:
                i+=1;
                continue;
            right.insert(0, num*right[0]);
            i+=1;
        print right

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(right[i+1])
            elif i == len(nums)-1:
                result.append(left[-2])
            else:
                result.append(left[i-1] * right[i+1])

        return result;


def main():
    solution = Solution();
    print solution.productExceptSelf([1,2,3,4]);

if __name__ == '__main__':
    main()
