def start_search(a, s, g):
    R = len(a)
    C = len(a[0])

    def isValid(x, y, v): 
        return 0 <= x < R and 0 <= y < C and a[x][y] == 1 and (x, y) not in v
    def dls(curr, limit, v, path):
        if (curr == g):
            path.append(curr)
            return True
        
        if limit <= 0:
            return False
        x, y = curr
        v.add((x, y))
        path.append((x, y))
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if isValid(nx, ny, v):
                if dls((nx, ny), limit - 1, v, path):
                    return True
        v.remove((x, y))
        path.pop()
        return False
    
    for d in range(R * C):
        visited = set()
        route = []
        if dls(s, d, visited, route):
            return d, route
    return -1, []

try:
    print("Grid size (rows columns):")
    r, c = map(int, input().split())
    matrix = []
    print(f"Enter {r} rows (1 for path, 0 for wall):")
    for i in range(r):
        matrix.append(list(map(int, input().split())))
    start_node = tuple(map(int, input("Start (r c): ").split()))
    goal_node = tuple(map(int, input("Target (r c): ").split()))
    d_val, path_res = start_search(matrix, start_node, goal_node)

    if d_val != -1:
        print("\nPath found at depth:", d_val)
        print("Path Traversal Order is:", path_res)
    else:
        print("\nNo path exists within max depth 6")
        
except Exception as e:
    print("Input error! Make sure you enter numbers correctly.")
