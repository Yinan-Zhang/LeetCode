

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def get_neighbors( x,y ):
            up   = (x, y-1) if y-1 >=0            else None;
            down = (x, y+1) if y+1 < len(grid[0]) else None;
            left = (x-1, y) if x-1 >=0            else None;
            right= (x+1, y) if x+1 < len(grid)    else None;
            results = [];
            if up    and grid[up[0]][up[1]]       == "1": results.append(up)
            if down  and grid[down[0]][down[1]]   == "1": results.append(down)
            if left  and grid[left[0]][left[1]]   == "1": results.append(left)
            if right and grid[right[0]][right[1]] == "1": results.append(right)
            return results;

        if grid is None: return 0;

        ones = [];
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == "1":
                    ones.append((x,y));

        visited = set([])
        island_count = 0;
        while len(ones) > 0:
            one = ones.pop();
            if one in visited: continue;

            to_visit = set([one]);
            while len(to_visit)>0:
                current = to_visit.pop();
                visited.add(current)
                neighbors = get_neighbors( current[0], current[1] )
                for neighbor in neighbors:
                    if neighbor not in visited:
                        to_visit.add(neighbor);
            island_count += 1;

        return island_count;


def main():
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]

    solution = Solution();
    print solution.numIslands(grid)


main();
