# link: https://www.acmicpc.net/problem/1001

import sys

def subtraction(A: int, B: int) -> int:
    """
    This function subtracts two integers A and B and prints out the result.
    It raises an error if not A > 0 or not B < 10.
    """
    if A <= 0:
        raise Exception("A should be an integer > 0")
    if B >= 10:
        raise Exception("B should be an integer < 10")
    return A - B

def main():
    # A = int(input("Enter A (should be an integer > 0): "))
    # B = int(input("Enter B (should be an integer < 10): "))
    A, B = map(int, sys.stdin.readline().strip().split())
    print(subtraction(A, B))

if __name__ == "__main__":
    main()
