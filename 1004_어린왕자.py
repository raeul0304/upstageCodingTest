# link: https://www.acmicpc.net/problem/1004

import sys
import math

def min_planets_entrance(x1: int, y1: int, x2: int, y2: int, Cx: int, Cy: int, r: int) -> int:
    # Calculate distances of both points to the center
    dp = math.sqrt((x1 - Cx) ** 2 + (y1 - Cy) ** 2)  # departing point
    ap = math.sqrt((x2 - Cx) ** 2 + (y2 - Cy) ** 2)  # arriving point

    # The only case where you count a border is if exactly one of the two points is within the planetary circle, meaning the path crosses the circle boundary.
    # If both points are inside or outside the circle, it doesn’t count as a crossing.
    # Check if only one of the points is inside the circle
    inside_departure = dp < r
    inside_arrival = ap < r

    # Return 1 if one point is inside and the other is outside, otherwise 0.
    return 1 if inside_departure != inside_arrival else 0

def main():
    num_testCases = int(sys.stdin.readline().strip())
    results = []
    for i in range(num_testCases):
        count = 0
        x1, y1, x2, y2 = map(int, sys.stdin.readline().strip().split())
        num_planets = int(sys.stdin.readline().strip())
        if not 1 <= num_planets <= 50:
                raise Exception("Number of planets should be an integer between 1 and 50 (both inclusive)")
        for j in range(num_planets):
            Cx, Cy, r = map(int, sys.stdin.readline().strip().split())
            if not all(-1000 <= value <= 1000 for value in (x1, y1, x2, y2, Cx, Cy)):
                raise Exception("x1, y1, x2, y2, Cx, and Cy should be integers between -1000 and 1000 (both inclusive)")
            if not 1 <= r <= 1000:
                raise Exception("r should be an integer between 1 and 1000 (both inclusive)")
            count += min_planets_entrance(x1, y1, x2, y2, Cx, Cy, r)
        # Store the result for this test case
        results.append(count)
    
    # Output all results after processing all test cases
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
