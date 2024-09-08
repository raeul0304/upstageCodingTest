# link: https://www.acmicpc.net/problem/1003

import sys

def fibonacciCount(n: int) -> None:
    zero = [1, 0]
    one = [0, 1]
    if n >= 2:
        for i in range(2, n+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print(f"{zero[n]} {one[n]}")

def main():
    print("Enter the number of test cases: ", end="")
    num_testCases = int(sys.stdin.readline().strip())
    if num_testCases > 40 or num_testCases < 0:
        raise Exception("N should be a positive integer that is <= 40 or 0")

    for i in range(num_testCases):
        print(f"Enter test case #{i+1}: ", end="")
        n = int(sys.stdin.readline().strip())
        fibonacciCount(n)

if __name__ == "__main__":
    main()
