from pyraminx import Pyraminx

def a():
    return 'solution'


def heuristic():
    return 'g()'

#heuristic: max(number colors per side) - 1
def ColorsPerSide(puzzle): 
    colors_per_side = []
    #iterate through each side
    for side in range(puzzle.array.shape[1]):
        colors = set()
        for triangle in range(puzzle.array.shape[0]):
            colors.add(puzzle.array[triangle][side])
        colors_per_side.append(len(colors))

    return max(colors_per_side) - 1
        




