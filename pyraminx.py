import numpy as np
import inspect
from copy import deepcopy
import tkinter as tk
from tkinter import *
import random


# Starting coordinates for each of the faces.
# Initially, A = red, B = blue, C = green, D = yellow (upside down)
FACE_A = (160, 60)
FACE_B = (640, 60)
FACE_C = (400, 60)
FACE_D = (400, 600)


"""
Triangle class to track each triangle's color. Necessary for visualization.
ID was used when bugfixing move functions.
"""
class Triangle:
    def __init__(self, color, id=None):
        self.color = color
        self.id = id
    
    def set_id(self, id):
        self.id = id

class Pyraminx:
    def __init__(self):
        row = np.array([Triangle("red"), Triangle("blue"), Triangle("green"), Triangle("yellow")])

        self.array = np.array([deepcopy(row) for _ in range(16)])

        for id, row in enumerate(self.array):  # enumerate provides the row index (id)
            for triangle in row:
                triangle.set_id(id)  # use the row index as id

    def print(self):
        for row in self.array:
            for item in row:
                print(f"'{item.color}' ", end="")
            print()

    def isSolved(self, puzzle) -> bool:
        for row in puzzle.array:
            if not (row[0].color == 'red' and row[1].color == 'blue' and row[2].color == 'green' and row[3].color == 'yellow'):
                return False
    
        return True

    """
    The following functions are legal moves in the 4x4x4 Pyraminx puzzle.
    We identified the index swaps to represent each move and implemented them in
    12 move functions. Each move function is clockwise respective to the center of the pyraminx.
    In order to do counter-clockwise moves, run the function twice.
    """
    def u(self):
        front_temp = deepcopy(self.array[0, 2])
        left_temp = deepcopy(self.array[0, 0])
        right_temp = deepcopy(self.array[0, 1])
        self.array[0, 2] = right_temp
        self.array[0, 0] = front_temp
        self.array[0, 1] = left_temp

    def U(self):
        front_temp = self.array[1:4, 2].copy()
        left_temp = self.array[1:4, 0].copy()
        right_temp = self.array[1:4, 1].copy()
        self.array[1:4, 2] = right_temp
        self.array[1:4, 0] = front_temp
        self.array[1:4, 1] = left_temp
        
    def Uw(self):
        front_temp = self.array[4:9, 2].copy()
        left_temp = self.array[4:9, 0].copy()
        right_temp = self.array[4:9, 1].copy()
        self.array[4:9, 2] = right_temp
        self.array[4:9, 0] = front_temp
        self.array[4:9, 1] = left_temp

    def l(self):
        front_temp = deepcopy(self.array[9, 2])
        left_temp = deepcopy(self.array[15, 0])
        bottom_temp = deepcopy(self.array[9, 3])
        self.array[9, 2] = left_temp
        self.array[15, 0] = bottom_temp
        self.array[9, 3] = front_temp

    def L(self):
        front_temp = []
        front_temp.append(deepcopy(self.array[4, 2]))
        front_temp.append(deepcopy(self.array[10, 2]))
        front_temp.append(deepcopy(self.array[11, 2]))
        left_temp = []
        left_temp.append(deepcopy(self.array[8, 0]))
        left_temp.append(deepcopy(self.array[13, 0]))
        left_temp.append(deepcopy(self.array[14, 0]))
        bottom_temp = []
        bottom_temp.append(deepcopy(self.array[4, 3]))
        bottom_temp.append(deepcopy(self.array[10, 3]))
        bottom_temp.append(deepcopy(self.array[11, 3]))
        #fixing bottom face
        self.array[11, 3] = front_temp[0]
        self.array[10, 3] = front_temp[1]
        self.array[4, 3] = front_temp[2]
        #fixing front face
        self.array[4, 2] = left_temp[1]
        self.array[10, 2] = left_temp[2]
        self.array[11, 2] = left_temp[0]
        #fixing left face
        self.array[8, 0] = bottom_temp[0]
        self.array[13, 0] = bottom_temp[1]
        self.array[14, 0] = bottom_temp[2]
        
    def Lw(self):
        front_temp = []
        front_temp.append(deepcopy(self.array[1, 2]))        
        front_temp.append(deepcopy(self.array[5, 2]))
        front_temp.append(deepcopy(self.array[6, 2]))
        front_temp.append(deepcopy(self.array[12, 2]))
        front_temp.append(deepcopy(self.array[13, 2]))        
        left_temp = []
        left_temp.append(deepcopy(self.array[3, 0]))
        left_temp.append(deepcopy(self.array[7, 0]))
        left_temp.append(deepcopy(self.array[6, 0]))
        left_temp.append(deepcopy(self.array[12, 0]))
        left_temp.append(deepcopy(self.array[11, 0]))
        bottom_temp = []
        bottom_temp.append(deepcopy(self.array[1, 3]))
        bottom_temp.append(deepcopy(self.array[5, 3]))
        bottom_temp.append(deepcopy(self.array[6, 3]))
        bottom_temp.append(deepcopy(self.array[12, 3]))
        bottom_temp.append(deepcopy(self.array[13, 3]))
        #fixing bottom face
        self.array[13, 3] = front_temp[0]
        self.array[12, 3] = front_temp[1]
        self.array[6, 3] = front_temp[2]
        self.array[5, 3] = front_temp[3]
        self.array[1, 3] = front_temp[4]
        #fixing front face
        self.array[1, 2] = left_temp[4]
        self.array[5, 2] = left_temp[3]
        self.array[6, 2] = left_temp[2]
        self.array[12, 2] = left_temp[1]
        self.array[13, 2] = left_temp[0]
        #fixing left face
        self.array[3, 0] = bottom_temp[0]
        self.array[7, 0] = bottom_temp[1]
        self.array[6, 0] = bottom_temp[2]
        self.array[12, 0] = bottom_temp[3]
        self.array[11, 0] = bottom_temp[4]

    def r(self):
        front_temp = self.array[15, 2]
        right_temp = self.array[9, 1]
        bottom_temp = self.array[15, 3]
        self.array[15, 2] = bottom_temp
        self.array[9, 1] = front_temp
        self.array[15, 3] = right_temp

    def R(self):
        front_temp = [(self.array[8, 2], self.array[14, 2], self.array[13, 2])].copy()
        right_temp = [(self.array[4, 1], self.array[10, 1], self.array[11, 1])].copy()
        bottom_temp = [(self.array[8, 3], self.array[14, 3], self.array[13, 3])].copy()
        #fixing front face
        self.array[13, 2] = bottom_temp[0][0]
        self.array[14, 2] = bottom_temp[0][1]
        self.array[8, 2] = bottom_temp[0][2]
        #fixing right face
        self.array[4, 1] = front_temp[0][2]
        self.array[10, 1] = front_temp[0][1]
        self.array[11, 1] = front_temp[0][0]
        #fixing bottom face
        self.array[8, 3] = right_temp[0][0]
        self.array[14, 3] = right_temp[0][1]
        self.array[13, 3] = right_temp[0][2]

    def Rw(self):
        front_temp = (self.array[3, 2], self.array[7, 2], self.array[6, 2], self.array[11, 2], self.array[12, 2])
        right_temp = (self.array[1, 1], self.array[5, 1], self.array[6, 1], self.array[12, 1], self.array[13, 1])
        bottom_temp = (self.array[3, 3], self.array[6, 3], self.array[7, 3], self.array[11, 3], self.array[12, 3])
        #fixing front face
        self.array[3, 2] = bottom_temp[4]
        self.array[7, 2] = bottom_temp[3]
        self.array[6, 2] = bottom_temp[2]
        self.array[12, 2] = bottom_temp[1]
        self.array[11, 2] = bottom_temp[0]
        #fixing right face
        self.array[1, 1] = front_temp[4]        
        self.array[5, 1] = front_temp[3]
        self.array[6, 1] = front_temp[2]
        self.array[12, 1] = front_temp[1]        
        self.array[13, 1] = front_temp[0]
        #fixing bottom face
        self.array[3, 3] = right_temp[0]
        self.array[6, 3] = right_temp[1]
        self.array[7, 3] = right_temp[2]
        self.array[12, 3] = right_temp[3]
        self.array[11, 3] = right_temp[4]
        
    def b(self):
        left_temp = deepcopy(self.array[9, 0])
        right_temp = deepcopy(self.array[15, 1])
        bottom_temp = deepcopy(self.array[0, 3])
        self.array[9, 0] = right_temp
        self.array[15, 1] = bottom_temp
        self.array[0, 3] = left_temp
        
    def B(self):
        left_temp = (self.array[4, 0], self.array[10, 0], self.array[11, 0])
        right_temp = (self.array[13, 1], self.array[14, 1], self.array[8, 1])
        bottom_temp = self.array[1:4, 3].copy()
        #fixing left side
        self.array[4, 0] = right_temp[0]
        self.array[10, 0] = right_temp[1]
        self.array[11, 0] = right_temp[2]
        #fixing bottom
        self.array[1, 3] = left_temp[0]
        self.array[2, 3] = left_temp[1]
        self.array[3, 3] = left_temp[2]
        #fixing right
        self.array[13, 1] = bottom_temp[0]
        self.array[14, 1] = bottom_temp[1]
        self.array[8, 1] = bottom_temp[2]

    def Bw(self):
        left_temp = (self.array[1, 0], self.array[5, 0], self.array[6, 0], self.array[12, 0], self.array[13, 0])
        right_temp = (self.array[11, 1], self.array[12, 1], self.array[6, 1], self.array[7, 1], self.array[3, 1])
        bottom_temp = self.array[4:9, 3].copy()
        #fixing left
        self.array[1, 0] = right_temp[0]
        self.array[5, 0] = right_temp[1]
        self.array[6, 0] = right_temp[2]
        self.array[12, 0] = right_temp[3]
        self.array[13, 0] = right_temp[4]
        #fixing bottom
        self.array[4, 3] = left_temp[0]
        self.array[5, 3] = left_temp[1]
        self.array[6, 3] = left_temp[2]
        self.array[7, 3] = left_temp[3]
        self.array[8, 3] = left_temp[4]
        #fixing right
        self.array[11, 1] = bottom_temp[0]
        self.array[12, 1] = bottom_temp[1]
        self.array[6, 1] = bottom_temp[2]
        self.array[7, 1] = bottom_temp[3]
        self.array[3, 1] = bottom_temp[4]
    
    def find_moves(self):
        members = inspect.getmembers(self.__class__, predicate=inspect.isfunction)
        non_moves = [Pyraminx.__init__, Pyraminx.print, Pyraminx.Randomize, Pyraminx.find_moves, Pyraminx.isSolved]
        moves = [func for name, func in members if func not in non_moves]
        return moves
    """
    Takes user input and makes that many clockwise moves in order to randomize the puzzle
    """
    def Randomize(self, num_moves):
        moves = self.find_moves()
        for i in range(num_moves):
            random_move = random.choice(moves)
            random_move(self)
            print(random_move)

"""
GUI class used to visualize the 4x4x4 Pyraminx
"""
class GUI:
    def __init__(self, root, pyraminx):
        self.root = root
        self.pyraminx = pyraminx
        root.title("Pyraminx Puzzle")

        self.canvas = Canvas(root, width=800, height=800, bg='white')
        self.canvas.pack()


        self.num_moves = IntVar()
        self.moves_entry = Entry(root, textvariable=self.num_moves)
        self.moves_entry.pack(side=RIGHT)

        self.button = Button(root, text="Randomize", command=self.visualizeRandomize)
        self.button.pack(side=RIGHT)

        self.updateBoard()

    """
    Iterate through faces, convert arrays to work with drawFace function
    """
    def updateBoard(self):
        faces = []
        for face in range(4):
            faces.append(self.pyraminx.array[:, face])
        
        for count, face in enumerate(faces):
            fixedFace = self.fixArrays(face)
            self.drawFace(fixedFace, count)
            
    
    """
    Function used to simplify building triangles
    Only did this so that updated structures were functional with already written drawing functions
    """
    def fixArrays(self, array):
        # Define the sizes of each row
        sizes = [1, 3, 5, 7]

        # Create an empty list to hold the result
        result = []

        # Index to track the current position in the array
        start_index = 0

        # Iterate over each size and slice the array accordingly
        for size in sizes:
            # Slice the array from start_index to start_index + size
            end_index = start_index + size
            result.append(array[start_index:end_index])
            # Update start_index for the next slice
            start_index = end_index
                
        result_array = np.array(result, dtype=object)
        return result_array


    """
    Function to draw all of the small triangles that make up each face
    """
    def drawFace(self, face, counter):
        #Build triangles left to right
        match counter:
            case 0:
                x, y = FACE_A
            case 1:
                x, y = FACE_B
            case 2:
                x, y = FACE_C
            case 3:
                x, y = FACE_D

        if counter == 3:
        #Bottom triangle is drawn upside down
            for row, list in enumerate(face):
                index = 0
                y = y - 60
                x = x - 30*(len(list)-1)
                for col, triangle in enumerate(list):
                    if col%2 == 1:
                        self.draw_sticker(x, y, triangle.color, triangle.id)
                    else:
                        self.draw_upsidedown_sticker(x, y, triangle.color, triangle.id)

                    x = x+30
                index = index+1
        else:
        #Drawing right-side up triangles
            for row, list in enumerate(face):
                y = y + 60
                x = x - 30*(len(list)-1)
                for col, triangle in enumerate(list):
                    if col%2 == 0:
                        self.draw_sticker(x, y, triangle.color, triangle.id)

                    else:
                        self.draw_upsidedown_sticker(x, y, triangle.color, triangle.id)

                    x = x+30
        
   
    def visualizeRandomize(self):
        self.pyraminx.Randomize(self.num_moves.get())
        self.updateBoard()

    def draw_sticker(self, x, y, color, id):
        size = 30
        x1 = x
        x2 = x - size
        x3 = x + size

        y1 = y - size
        y2 = y + size
        y3 = y + size

        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color, outline='black')
        self.canvas.create_text(x, y, text=str(id))

    def draw_upsidedown_sticker(self, x, y, color, id):
        size = 30
        x1 = x
        x2 = x - size
        x3 = x + size

        y1 = y + size
        y2 = y - size
        y3 = y - size

        self.canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color, outline='black')
        self.canvas.create_text(x, y, text=str(id))



def main():
    root = Tk()
    root.resizable(0,0)
    pyraminx = Pyraminx()
    app = GUI(root, pyraminx)
    root.mainloop()


if __name__ == "__main__":
    main()