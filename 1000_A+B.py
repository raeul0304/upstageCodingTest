# link: https://www.acmicpc.net/problem/1000

A = int(input("Enter A (should be an integer > 0): "))
B = int(input("Enter B (should be an integer < 10): "))

def addition(A: int, B: int) -> int:
    """
    This function adds two integers A and B and prints out the result.
    It raises an error if not A > 0 or not B < 10.
    """
    if A <= 0:
        raise Exception("A should be an integer > 0")
    if B >= 10:
        raise Exception("B should be an integer < 10")
    print(A + B)

addition(A, B)
