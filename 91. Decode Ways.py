class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_ = { val-ord('A')+1 : chr(val) for val in range(ord('A'), ord('Z')+1) };

        # Dynamic planning:
        # let decode(s) = s[0] + decode(s[1, n]) + s[0,2] + decode(s[2,n])
         

        pass;


def main():
    solution = Solution();
    print solution.numDecodings("12")

if __name__ == '__main__':
    main()
