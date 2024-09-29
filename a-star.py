from pyraminx import Pyraminx
import heapq
from copy import deepcopy
import numpy as np

# PuzzleState class implemented so that minheap does not try to compare Pyraminx objects
class PuzzleState:
    def __init__(self, puzzle, path):
        self.puzzle = puzzle
        self.path = path

    def __lt__(self, other):
        # If two states have the same f value, break tie via path length
        return len(self.path)
"""
A* algorithm:
    Iterates through states to find the path to a solution state.
params:
    puzzle (Pyraminx): Pyraminx puzzle randomized with k random moves.

returns:
    path (list): Legal moves on the pyraminx in order to bring the randomized state to solve state
    move_num (int): Number of nodes expanded on the tree when solution is found
"""
def astar(puzzle):
    pq = []
    visited = set()

    root = deepcopy(puzzle)
    g = 0
    h = ColorsPerSide(root)
    f = g + h
    path = []


    #min heap stores f, g, config, and path
    start = (f, g, PuzzleState(root, path))
    heapq.heappush(pq, start)
    visited.add(root.extract_array())
    move_num = 0

    while pq:
        f, g, puzzle = heapq.heappop(pq)
        config = puzzle.puzzle
        path = puzzle.path

        if config.isSolved(): #if node is in solved state, return path and # of nodes expanded on the tree
            return path, move_num
        
        for move in config.find_moves(): #check all 12 children of each state and calculate heuristic
            new_state = deepcopy(config)
            new_state = make_move(new_state, move)
            new_g = g + 1
            new_f = ColorsPerSide(new_state) + len(path)
            new_path = path + [move]

            new_node = (new_f, new_g, PuzzleState(new_state, new_path))
            move_num = move_num + 1

            if new_state.extract_array() not in visited: #if we find a new state, store it in the heap
                heapq.heappush(pq, new_node)
                visited.add(new_state.extract_array())

    return None #no solution found

#heuristic: max(number colors per side) - 1
"""
ColorsPerSide:
    Finds the maximum # of colors on any of the faces in the puzzle. This is our heuristic function
    used to guide A* to a solution.
params:
    puzzle (Pyraminx): Pyraminx object to be checked
returns:
    max value in colors_per_side (int)
"""
def ColorsPerSide(puzzle: Pyraminx) -> int: 
    colors_per_side = []
    #iterate through each side
    for side in range(puzzle.array.shape[1]):
        colors = set()
        for triangle in range(puzzle.array.shape[0]):
            colors.add(puzzle.array[triangle, side].color) # Add unique colors to set
        colors_per_side.append(len(colors)) #Store unique colors on each face in list

    return max(colors_per_side) - 1

"""
In order to reduce the solution space, we have decided to randomize only using clockwise moves.
When we solve, we run these clockwise moves twice in order to simulate a counter-clockwise move.
"""
def make_move(puzzle: Pyraminx, move):
    move(puzzle)
    move(puzzle)
    return puzzle

"""
GenerateRandomInstances:
    Creates a list of 5 Pyraminx objects randomized by k moves.
params:
    k (int): number of moves to randomize Pyraminx with
returns:
    random_puzzles (list): list of randomized Pyraminx objects
"""
def GenerateRandomInstances(k: int) -> list:
    random_puzzles = []
    
    for _ in range(5):
        puzzle = Pyraminx()
        puzzle.Randomize(k)
        random_puzzles.append(puzzle)

    return random_puzzles


def main():
    puzzles = GenerateRandomInstances(6) # Create 5 randomized puzzles
    puz = []
    
    #Iterate through randomized puzzles and print # of unique colors per side for each puzzle
    for i in range(len(puzzles)):
        colors_per_side = ColorsPerSide(puzzles[i])
        puz.append(colors_per_side)
    print(puz)

    #Use A* to solve each puzzle. Print the path to solve and the width of tree when solution is found.
    for puzzle in puzzles:
        path, width = astar(puzzle)
        print(f'path: {path}, width at solution: {width}')


if __name__ == "__main__":
    main()

