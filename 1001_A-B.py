# link: https://www.acmicpc.net/problem/1001

A = int(input("Enter A (should be an integer > 0): "))
B = int(input("Enter B (should be an integer < 10): "))

def subtraction(A: int, B: int) -> int:
    """
    This function subtracts two integers A and B and prints out the result.
    It raises an error if not A > 0 or not B < 10.
    """
    if A <= 0:
        raise Exception("A should be an integer > 0")
    if B >= 10:
        raise Exception("B should be an integer < 10")
    print(A - B)

subtraction(A, B)
