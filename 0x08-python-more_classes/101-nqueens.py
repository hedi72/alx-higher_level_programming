#!/usr/bin/python3
import sys

def isSafe(board, row, col, n):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solveNQueens(board, col, n):
    if col == n:
        print(board)
        return
    for row in range(n):
        if isSafe(board, row, col, n):
            board[col] = row
            solveNQueens(board, col + 1, n)
            board[col] = -1

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    board = [-1 for i in range(n)]
    solveNQueens(board, 0, n)
