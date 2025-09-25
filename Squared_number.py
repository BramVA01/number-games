original_number = 2

def square(number):
    return number**2


print(square(original_number))


def main():
    print(square(original_number))
    print(give_solutions(limit_to_z))


limit_to_z = 20
"""def give_solutions(limit):
    sol =[]
    for i in range(0,limit):
        equation = Eq(x**2 + y**2 - i**2)
        sol = [sol,solve(equation)]
    return sol"""

def give_solutions(limit):
    """
    1. Initialize
    2. Loops
    3. Loops
    4. Loops
    5. Checks
    6. Returns
    """
    solutions = []
    for i in range(1,limit):
        for x in range(1,limit):
            for y in range(1,limit):
                if x**2 + y**2 == i**2:
                    solutions.append([x,y,i])
    return [solutions]


if __name__ == "__main__":
    main()


"""if pythagorean_triplets(limit):
"""
#dededede