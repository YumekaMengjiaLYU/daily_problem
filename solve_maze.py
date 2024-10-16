def paths_through_maze(maze):
    visited = set()
    result = 0
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    num_of_rows, num_of_cols = len(maze), len(maze[0])

    def find_paths(row, col):
        nonlocal result
        # if we reach bottom right, then we add 1 to result
        if row == num_of_rows - 1 and col == num_of_cols - 1:
            result += 1
            return 
        visited.add((row, col))
        for dir in directions:
            next_row, next_col = tuple(map(lambda i, j: i + j, (row, col), dir))
            if is_valid(next_row, next_col):
                find_paths(next_row, next_col)

        visited.remove((row, col))

    def is_valid(row, col):
        return row >= 0 and col >= 0 and row < num_of_rows and \
        col < num_of_cols and not maze[row][col] and (row, col) not in visited
    
    find_paths(0,0)
    return result

if __name__ == "__main__":
    maze = [[0,1,0],[0,0,1],[0,0,0]]
    result = paths_through_maze(maze)
    print(result)