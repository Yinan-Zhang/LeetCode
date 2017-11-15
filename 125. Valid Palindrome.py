class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_cp = ""
        for char in s:
            if char.lower().isalnum():
                s_cp += char.lower();
        l, r = 0, 0
        s = s_cp
        s1 = s;
        s2 = s[::-1]

        while l + r < len(s):
            if s1[l].lower() != s2[r].lower():
                return False
            l +=1;
            r += 1
        return True

def main():
    solution = Solution()
    print solution.isPalindrome(" ");

if __name__ == '__main__':
    main()
