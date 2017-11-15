class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        chars = {x : chr(x) for x in range(ord('A'), ord('Z')+1)}
        while n > 0:
            result.insert( 0, chars[(n-1) % 26 + ord('A')] );
            n-=1
            n /= 26;

        return ''.join(result)

def main():
    solution = Solution();
    print solution.convertToTitle(26)
    pass;

if __name__ == '__main__':
    main()
