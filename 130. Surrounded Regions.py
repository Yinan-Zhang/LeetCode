def solve(board):
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def neighbor_crosses(i,j):
        N = (i-1,j) if i > 0 else None;
        E = (i,j+1) if j+1 < len(board[0]) else None;
        S = (i+1,j) if i+1 < len(board) else None;
        W = (i,j-1) if j > 0 else None;

        neighbors = [];
        if N and board[N[0]][N[1]]== 'X': neighbors.append(N);
        if E and board[E[0]][E[1]]== 'X': neighbors.append(E);
        if S and board[S[0]][S[1]]== 'X': neighbors.append(S);
        if W and board[W[0]][W[1]]== 'X': neighbors.append(W);

        return neighbors;

    def neighbor_circles(i,j):
        N = (i-1,j) if i > 0 else None;
        E = (i,j+1) if j+1 < len(board[0]) else None;
        S = (i+1,j) if i+1 < len(board) else None;
        W = (i,j-1) if j > 0 else None;

        neighbors = [];
        if N and board[N[0]][N[1]]== 'O': neighbors.append(N);
        if E and board[E[0]][E[1]]== 'O': neighbors.append(E);
        if S and board[S[0]][S[1]]== 'O': neighbors.append(S);
        if W and board[W[0]][W[1]]== 'O': neighbors.append(W);

        return neighbors

    def neighbor_empty(i,j):
        N = (i-1,j) if i > 0 else None;
        E = (i,j+1) if j+1 < len(board[0]) else None;
        S = (i+1,j) if i+1 < len(board) else None;
        W = (i,j-1) if j > 0 else None;

        neighbors = [];
        if N is None or board[N[0]][N[1]]== ' ': neighbors.append(N);
        if E is None or board[E[0]][E[1]]== ' ': neighbors.append(E);
        if S is None or board[S[0]][S[1]]== ' ': neighbors.append(S);
        if W is None or board[W[0]][W[1]]== ' ': neighbors.append(W);

        return neighbors

    circles = [];
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'O':
                circles.append((i,j))

    visited = set([]);
    components = [];

    for i,j in circles:
        if not (i,j) in visited:
            component = set([(i,j)]);
            unvisited_neighbors = set(neighbor_circles(i,j));
            while len(unvisited_neighbors) > 0:
                ni, nj = unvisited_neighbors.pop();
                component.add((ni,nj));
                neighors = neighbor_circles(ni, nj);
                for n in neighors:
                    if not n in component:
                        unvisited_neighbors.add(n);
            print component
            components.append(component)
            visited = visited.union(component)


    to_flip = []
    for component in components:
        flip = True;
        for i,j in component:
            empties = neighbor_empty(i,j);
            if len(empties) > 0:
                flip = False;
        if flip:
            for i,j in component:
                to_flip.append((i,j));

    for i,j in to_flip:
        row = board[i];
        row = row[:j] + ["X"] + row[j+1:]
        board[i] = row;

    print board

def test():
    case = ["XXOX",
            "XOOO",
            "XXOX",
            "XOXX"]
    solve(case);

test()
