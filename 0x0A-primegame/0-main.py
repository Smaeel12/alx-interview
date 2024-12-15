#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


# print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

def test_isWinner():
    test_cases = [
        ((3, [3, 4, 5]), "Ben"),
        ((2, [5, 6]), "Maria"),
        ((4, [7, 8, 9, 10]), "Ben"),
        ((3, [11, 12, 13]), "Maria"),
        ((2, [14, 15]), "Ben"),
    ]

    for inputs, expected in test_cases:
        x, nums = inputs
        result = isWinner(x, nums)
        if result != expected:
            print(f"Test case failed: For inputs {inputs}, expected {expected}, but got {result}")
            return

    print("All test cases passed!")

# Call the tester function
test_isWinner()
