

class Solution(object):

    def __init__(self):
        self.results = set([]);

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s is None or len(s) == 0: return "";

        rmR = 0;    # number of ) to remove
        rmL = 0;    # number of ( to remove
        for char in s:
            if char == "(":
                rmL += 1;
            elif char == ")":
                if rmL > 0: rmL -= 1;
                else: rmR += 1;

        self.dfs(s, "", 0, rmR, rmL, 0)
        return list(self.results);

    def dfs(self, s, current_str, curr_idx, rmR, rmL, open):
        if rmR < 0 or rmL < 0 or open<0: return;
        print current_str, curr_idx, rmR, rmL

        if curr_idx == len(s) and rmR == 0 and rmL == 0 and open == 0:
            self.results.add(current_str);
            return;
        if curr_idx == len(s): return;

        if s[curr_idx] == '(':
            self.dfs(s, current_str+"(", curr_idx+1, rmR, rmL, open+1);     # Not remove this (
            self.dfs(s, current_str,     curr_idx+1, rmR, rmL-1, open);     # remove this (
        elif s[curr_idx] == ')':
            self.dfs(s, current_str+")", curr_idx+1, rmR, rmL, open-1);     # Not remove this )
            self.dfs(s, current_str,     curr_idx+1, rmR-1, rmL, open);     # remove this )
        else:
            self.dfs(s, current_str+s[curr_idx], curr_idx+1, rmR, rmL, open);  # remove this )


def main():
    solution = Solution();
    print solution.removeInvalidParentheses("(a)())()")

main();
