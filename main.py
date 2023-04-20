import heapq as hq


# This function reads a maze from a text file and return it as a 2D array
def read_maze_2d(file):
    maze = []
    with open(file) as f:
        for line in f:
            row = []
            # Loop through each character in the line, except for the last (which is a newline character)
            for char in line[:-1]:
                row.append(char)
            maze.append(row)
    return maze


def solve_maze(maze):
    # Create a set of all cells in the maze
    maze_cells = {(i, j) for i in range(len(maze)) for j in range(len(maze[i]))}
    # Finds the starting cell in the maze
    start = None
    end = None

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
                break
        if start:
            break

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'G':
                end = (i, j)
                break
        if end:
            break

    # Create a minimum heap of unvisited cells, with the starting cell at distance 0
    unvisited = [(0, start)]
    # Create an empty dictionary to store the visited cells and their distances from the starting cell
    visited = {}

    # While there are unvisited cells in the heap
    while unvisited:
        # Get the cell with the smallest distance from the heap
        currDist, currCell = hq.heappop(unvisited)
        # If the cell has already been visited, skip it
        if currCell in visited:
            continue
        # Mark the cell as visited and record its distance from the starting cell
        visited[currCell] = currDist
        # If the current cell is the end cell, than end the loop
        if maze[currCell[0]][currCell[1]] == 'G':
            break
        # Explores the neighbors of the current cell
        for direction in 'URDL': # Up, Right, Down, Left
            # Calculate the coordinates of the neighbor cell in the given direction
            if direction == 'U':
                childCell = (currCell[0] - 1, currCell[1])
            elif direction == 'R':
                childCell = (currCell[0], currCell[1] + 1)
            elif direction == 'D':
                childCell = (currCell[0] + 1, currCell[1])
            elif direction == 'L':
                childCell = (currCell[0], currCell[1] - 1)
            # If the neighbor cell is not a valid cell, skip it
            if childCell not in maze_cells:
                continue
            # Calculate the distance to the neighbor cell and add it to the heap
            toAdd = maze[childCell[0]][childCell[1]]
            if toAdd == 'X':
                continue
            if toAdd.isdigit():
                tempDist = currDist + int(toAdd)
            else:
                tempDist = visited[currCell]
            hq.heappush(unvisited, (tempDist, childCell))

    # Result will be the distance saved in the end cell
    return visited[end]


print(f"Solution 11x11 = {solve_maze(read_maze_2d('mazes/maze_11x11.txt'))}")
print(f"Solution 31x31 = {solve_maze(read_maze_2d('mazes/maze_31x31.txt'))}")
print(f"Solution 101x101 = {solve_maze(read_maze_2d('mazes/maze_101x101.txt'))}")
