from pyraminx import Pyraminx
import heapq
from copy import deepcopy
import numpy as np

class PuzzleState:
    def __init__(self, puzzle, path):
        self.puzzle = puzzle
        self.path = path

    def __lt__(self, other):
        # We don't want to compare PuzzleState objects, so this just always returns False
        return len(self.path)

def astar(puzzle, max_iterations):
    pq = []
    visited = set()

    root = deepcopy(puzzle)
    g = 0
    h = ColorsPerSide(root)
    f = g + h
    path = []


    #priority queue stores f, config, and path
    start = (f, g, PuzzleState(root, path))
    heapq.heappush(pq, start)
    visited.add(root.array.tobytes())
    move_num = 0
    iteration = 0
    while pq and move_num < max_iterations:
        f, g, puzzle = heapq.heappop(pq)
        config = puzzle.puzzle
        path = puzzle.path

        if config.isSolved():
            return path
        for move in config.find_moves():
            new_state = deepcopy(config)
            new_state = make_move(new_state, move)
            new_g = g + 1
            new_f = ColorsPerSide(new_state) + len(path)
            print(f'move: {move}, new_f {new_f}, move: {move_num}')
            new_path = path + [move]

            new_node = (new_f, new_g, PuzzleState(new_state, new_path))
            if all(not np.array_equal(new_state.array, array) for array in visited) :
                heapq.heappush(pq, new_node)
                visited.add(new_state.array.tobytes())
        move_num = move_num + 1
        iteration = iteration + 1
    return None #no solution found

def out_of_place_triangles(puzzle: Pyraminx) -> int:
    # Define the solved state (correct colors for each row/triangle)
    solved_colors = [
        ["red", "blue", "green", "yellow"] for _ in range(16)
    ]  # Assuming a 4x4 grid of 16 rows, each with 4 triangles of specific colors.

    # Count the number of out-of-place triangles
    out_of_place_count = 0

    # Iterate through each triangle in the current puzzle state
    for row_idx, row in enumerate(puzzle.array):
        for col_idx, triangle in enumerate(row):
            expected_color = solved_colors[row_idx][col_idx]
            if triangle.color != expected_color:
                out_of_place_count += 1

    return out_of_place_count

#heuristic: max(number colors per side) - 1
def ColorsPerSide(puzzle: Pyraminx) -> int: 
    colors_per_side = []
    #iterate through each side
    for side in range(puzzle.array.shape[1]):
        colors = set()
        for triangle in range(puzzle.array.shape[0]):
            colors.add(puzzle.array[triangle, side].color)
        colors_per_side.append(len(colors))
        #print(colors)

    return max(colors_per_side) - 1

def make_move(puzzle: Pyraminx, move):
    move(puzzle)
    move(puzzle)
    return puzzle

def create_tuple(h: int, puzzle: Pyraminx, path: list) -> tuple:
    return tuple(h, puzzle, path)


def GenerateRandomInstances(k: int) -> list:
    random_puzzles = []
    
    for _ in range(5):
        puzzle = Pyraminx()
        puzzle.Randomize(k)
        random_puzzles.append(puzzle)

    return random_puzzles

def main():
    puzzles = GenerateRandomInstances(6)
    puz = []
    for i in range(len(puzzles)):
        colors_per_side = ColorsPerSide(puzzles[i])
        puz.append(colors_per_side)
    print(puz)

    path = astar(puzzles[0], 10000)
    print(path)


if __name__ == "__main__":
    main()

