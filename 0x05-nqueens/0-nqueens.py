#!/usr/bin/python3
"""Solves the N Queens problem using backtracking"""

import sys


def is_safe(row, col, solution):
    """Check if placing a queen at (row, col) is safe"""
    for r, c in solution:
        if c == col or r - c == row - col or r + c == row + col:
            return False
    return True


def solve_nqueens(n, row=0, solution=[], results=[]):
    """Backtracking function to find all solutions"""
    if row == n:
        results.append(solution.copy())
        return

    for col in range(n):
        if is_safe(row, col, solution):
            solution.append([row, col])
            solve_nqueens(n, row + 1, solution, results)
            solution.pop()


def main():
    """Main entry point of the program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    results = []
    solve_nqueens(n, results=results)

    for solution in results:
        print(solution)


if __name__ == "__main__":
    main()
