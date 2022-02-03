# Created by: Zack Isingoma
# Created on: 30th Jan 2022.
# Sorts a list and displays the smallest
# number in the list


import random


def find_min_value(rand_numbers):
    total = 0
    for numbers in range(0, len(rand_numbers)):
        total = rand_numbers[numbers]
    return total


def main():

    numbers_array = []

    for randoms in range(0, 10):
        single_int = random.randint(0, 100)
        numbers_array.append(single_int)
        numbers_array.sort()
    print("In the list of numbers {} ".format(numbers_array), end="")
    print("The smallest number in the array is ")
    print(numbers_array[0])


if __name__ == "__main__":
    main()
