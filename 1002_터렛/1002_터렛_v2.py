# link: https://www.acmicpc.net/problem/1002

import sympy as sym
import sys

def circles_intersections(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) -> int:
    """
    This function finds the number of intersections of two circles using a python library SymPy.
    """
    
    # condition check
    if not all(-10000 <= value <= 10000 for value in (x1, y1, x2, y2)):
        raise Exception("x1, y1, x2, and y2 should be integers between -10000 and 10000 (both inclusive)")
    if not all(1 <= value <= 10000 for value in (r1, r2)):
        raise Exception("r1 and r2 should be integers between 1 and 10000 (both inclusive)")

    x = sym.Symbol('x')
    y = sym.Symbol('y')
    equations = [(x-x1) ** 2 + (y-y1) ** 2 - r1 ** 2, (x-x2) ** 2 + (y-y2) ** 2 - r2 ** 2]
    solutions = sym.solve(equations, (x, y))

    if len(solutions) > 2: return -1
    return len(solutions)

def main():
    print("Enter the number of test cases: ", end="")
    num_testCases = int(sys.stdin.readline().strip())
    for i in range(num_testCases):
        print(f"Enter test case #{i+1}: ", end="")
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
        print(circles_intersections(x1, y1, r1, x2, y2, r2))

if __name__ == "__main__":
    main()
