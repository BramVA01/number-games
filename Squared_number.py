import time
import numpy as np

original_number = 2

def square(number):
    return number**2

print(square(original_number))

limit_to_z = 100


def main():
    start_time = time.time()
    print(square(original_number))
    print(give_solutions(limit_to_z))
    end_time = time.time()

    print(end_time - start_time)




def give_solutions(limit: int) -> tuple([tuple([int])]):
    """
    1. Initialize
    2. Loops
    3. Loops
    4. Loops
    5. Checks
    6. Returns
    """

    if not isinstance(limit, int):
        raise TypeError("Limit is of the wrong type")

    solutions = []
    singles = np.arange(1,limit)
    squares = singles ** 2

    for i in squares:
        for x in squares:
            for y in squares:
                if x + y == i:
                    solutions.append([x,y,i])
    return np.sqrt(solutions)
    



if __name__ == "__main__":
    main()


"""if pythagorean_triplets(limit):
"""
#dededede