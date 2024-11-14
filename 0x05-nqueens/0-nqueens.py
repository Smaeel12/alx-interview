#!/usr/bin/python3
<<<<<<< HEAD
"""N-Queens Problem Solver"""
import sys


def solve_queens_problem(board_size):
    """Find all solutions to the N-Queens problem for a given board size"""

    def is_valid_position(current_column, placedClm):
        """Check if the current position is valid for placing a queen"""
        for row in range(len(placedClm)):
            if (
                placedClm[row] == current_column or
                placedClm[row] - row == current_column - len(placedClm) or
                placedClm[row] + row == current_column + len(placedClm)
            ):
                return False
        return True

    def place_queens(board_size, current_row, placedClm, solutions):
        """Recursively place queens on the board"""
        if current_row == board_size:
            solutions.append(placedClm[:])
            return

        for column in range(board_size):
            if is_valid_position(column, placedClm):
                placedClm.append(column)
                place_queens(board_size, current_row + 1, placedClm, solutions)
                placedClm.pop()

    solutions = []
    place_queens(board_size, 0, [], solutions)
    return solutions


def main():
    """Main function to handle input and output"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        board_size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_queens_problem(board_size)
    for solution in solutions:
        print([[row, solution[row]] for row in range(len(solution))])


if __name__ == "__main__":
    main()
=======
"""
Solution to the nqueens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    backtrack function to find solution
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
>>>>>>> 9e7dbec5432891283a6f47e2f5a5ce1b1bb30117
