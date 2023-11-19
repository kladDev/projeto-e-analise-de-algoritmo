import copy
import numpy as np


class Node:
    def __init__(self, board, pos):
        self.movements = [np.array([2, 1]),
                          np.array([1, 2]),
                          np.array([-1, 2]),
                          np.array([-2, 1]),
                          np.array([-2, -1]),
                          np.array([-1, -2]),
                          np.array([1, -2]),
                          np.array([2, -1])]
        self.board = board
        self.pos = pos
        self.children = []

    def is_valid(self, mov):
        new_pos = self.pos+mov
        n = len(self.board)-1
        if (new_pos[0] < 0 or new_pos[0] > n or new_pos[1] < 0 or new_pos[1] > n):
            return False
        return True

    def generate_children(self):
        if sum(sum(self.board)) == len(self.board)*len(self.board):
            print_board(self.board)
            return  # Problema solucionado

        print_board(self.board)
        for mov in self.movements:
            if self.is_valid(mov):
                new_pos = self.pos+mov
                if (self.board[new_pos[0]][new_pos[1]] == 0):
                    child_board = copy.deepcopy(self.board)
                    child_board[new_pos[0]][new_pos[1]] = 1
                    self.children.append(Node(child_board, new_pos))

        for child in self.children:
            child.generate_children()


def print_board(board):
    for row in board:
        print(" ".join(str(row)))
    print('- '*len(row))


def solve_knight():
    for i in range(5):
        for j in range(5):
            root = Node(np.zeros((5, 5)), np.array([i, j]))
            root.generate_children()


solve_knight()