from pyraminx import Pyraminx
import heapq

def astar(puzzle):
    config = create_tuple(puzzle)
    heapq.pushheap(config)

    #while not heapq.empty():

    return 0



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


def create_tuple(puzzle):
    h = ColorsPerSide(puzzle)
    return tuple(h, puzzle)


def GenerateRandomInstances(k: int):
    random_puzzles = []
    
    for _ in range(5):
        puzzle = Pyraminx()
        puzzle.Randomize(k)
        random_puzzles.append(puzzle)

    return random_puzzles

def main():
    puzzles = GenerateRandomInstances(4)
    puz = []
    for i in range(len(puzzles)):
        colors_per_side = ColorsPerSide(puzzles[i])
        puz.append(colors_per_side)
    print(puz)


if __name__ == "__main__":
    main()

