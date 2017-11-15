class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_ = { val-ord('A')+1 : chr(val) for val in range(ord('A'), ord('Z')+1) };
        if s is None or len(s) == 0: return 0;
        if s[0] == "0": return 0;


        # Dynamic planning:
        # let decode(s) = decode(s[-1]) + decode(s[0:n-1]) + decode(s[n-2 : ]) + decode(s[0:n-2])
        d = [0] * (len(s)+1);

        d[0] = d[1] = 1;
        for i in range(1, len(s)):
            if 9 < int(s[i-1]+s[i]) < 27:
                d[i+1] += d[i-1];
            if 0 < int(s[i]):
                d[i+1] += d[i];
        return d[-1]


def main():
    solution = Solution();
    print solution.numDecodings("123")

if __name__ == '__main__':
    main()
