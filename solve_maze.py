def paths_through_maze(maze):
    result = 0
    paths = []
    directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    num_of_rows, num_of_cols = len(maze), len(maze[0])

    def find_paths(row, col, current_path):
        nonlocal result
        nonlocal directions
        if row == num_of_rows - 1 and col == num_of_cols - 1:
            result += 1
            paths.append(current_path + [(row, col)])
            return
                
        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc
            if is_valid(next_row, next_col, current_path):
                find_paths(next_row, next_col, current_path + [(row, col)])

    def is_valid(row, col, current_path):
        return 0 <= row < num_of_rows and 0 <= col < num_of_cols and \
        (maze[row][col] == 0) and (row, col) not in current_path
    
    find_paths(0,0,[])
    return result

if __name__ == "__main__":
    maze = [[0,1,0],[0,0,1],[0,0,0]]
    result = paths_through_maze(maze)
    print(result)