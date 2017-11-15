class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        prev_str = None;
        for i in range(1, n+1):
            if i == 1:
                prev_str = "1"
            else:
                prev_str = self.helper(prev_str)
        return prev_str

    def helper(self, str_):
        count = []
        for char in str_:
            if len(count) == 0 :
                count.append( [1, char] )
            elif char == count[-1][1]:
                count[-1][0] += 1;
            else:
                count.append( [1, char] )
        result = ""
        for elem in count:
            result += str(elem[0]) + str(elem[1]);
        return result;



def main():
    solution = Solution();
    print solution.countAndSay(20)

main();
