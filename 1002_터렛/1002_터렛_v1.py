# link: https://www.acmicpc.net/problem/1002

import math
import sys

def circles_intersections(x1: int, y1: int, r1: int, x2: int, y2: int, r2: int) -> int:
    """
    This function finds the number of intersections of two circles algebraically.
    Refer to the following page for the algebra which is detailed under section "Intersection of two circles"
    -> https://paulbourke.net/geometry/circlesphere/
    """
    
    # condition check
    if not all(-10000 <= value <= 10000 for value in (x1, y1, x2, y2)):
        raise Exception("x1, y1, x2, and y2 should be integers between -10000 and 10000 (both inclusive)")
    if not all(1 <= value <= 10000 for value in (r1, r2)):
        raise Exception("r1 and r2 should be integers between 1 and 10000 (both inclusive)")

    # distance between origins
    d = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))      # d = math.dist([x1, y1], [x2, y2])

    # If d > r1 + r2 then there are no solutions, the circles are separate.
    # If d < |r1 - r2| then there are no solutions because one circle is contained within the other.
    if d > r1 + r2 or d < abs(r1 - r2):
        return 0
    # If d = 0 and r1 = r2 then the circles are coincident and there are an infinite number of solutions.
    if d == 0 and r1 == r2:
        return -1
    
    a = (r1 ** 2 - r2 ** 2 + d ** 2) / (2 * d)
    h = math.sqrt(r1 ** 2 - a ** 2)
    # point P2
    x3 = x1 + a * (x2 - x1) / d
    y3 = y1 + a * (y2 - y1) / d
    # 1st intersection point
    x4 = x3 + h * (y2 - y1) / d
    y4 = y3 - h * (x2 - x1) / d
    # 2nd intersection point
    x5 = x3 - h * (y2 - y1) / d
    y5 = y3 + h * (x2 - x1) / d

    # check if 1st intersection == 2nd intersection
    if x4 == x5 and y4 == y5:
        return 1
    else:
        return 2

def main():
    print("Enter the number of test cases: ", end="")
    num_testCases = int(sys.stdin.readline().strip())
    for i in range(num_testCases):
        print(f"Enter test case #{i+1}: ", end="")
        x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().strip().split())
        print(circles_intersections(x1, y1, r1, x2, y2, r2))

if __name__ == "__main__":
    main()
