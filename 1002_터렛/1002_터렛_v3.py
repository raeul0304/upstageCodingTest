# link: https://www.acmicpc.net/problem/1002
# reference: https://www.bbc.co.uk/bitesize/guides/z9pssbk/revision/4

import sys
import math

def circles_intersections(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) -> int:
    """
    This function finds the number of intersections of two circles NOT using python external libraries but in a naive way.
    """
    
    # condition check
    if not all(-10000 <= value <= 10000 for value in (x1, y1, x2, y2)):
        raise Exception("x1, y1, x2, and y2 should be integers between -10000 and 10000 (both inclusive)")
    if not all(1 <= value <= 10000 for value in (r1, r2)):
        raise Exception("r1 and r2 should be integers between 1 and 10000 (both inclusive)")

    # infinitely many intersections (circles coincide)
    if x1 == x2 and y1 == y2 and r1 == r2: return -1

    # 1 intersection (circles touch)
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))      # distance between origins
    if d == r1 + r2 or d == abs(r1 - r2): return 1

    # 2 intersections
    if abs(r1 - r2) < d < r1 + r2: return 2

    # else cases (i.e. 0 intersection)
    return 0

def main():
    print("Enter the number of test cases: ", end="")
    num_testCases = int(sys.stdin.readline().strip())
    for i in range(num_testCases):
        print(f"Enter test case #{i+1}: ", end="")
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
        print(circles_intersections(x1, y1, r1, x2, y2, r2))

if __name__ == "__main__":
    main()
