import random


def binary_search(my_list, number):
    low, high = 0, len(my_list) - 1
    counter = 0

    while low < high:
        counter += 1
        print(f'VALUE HIGH: {high}, LOW: {low}')
        mid = (low + high) // 2
        print(f'VALUE OF MID: {mid}')

        if mid == number:
            return f'VALUE FOUND: {mid}, in {counter} attempts!!'
        if mid < number:
            low = mid + 1
        if mid > number:
            high = mid - 1

    return f'VALUE FOUND: {low}, in {counter} attempts'


def shift_my_list(my_list, shift: int = 1) -> list:
    """
    Rotates list last number to index 0
    :param my_list: list to be rotated
    :param shift: number of times the list in being rotated. I cannot be a higher number than list length.
    :return: Returns rotated list.
    """
    # Modulus prevents unnecessary rotations. Also, slicing and concatenating the list is faster than using a for loop
    shift = shift % len(my_list)
    return my_list[- shift:] + my_list[: - shift]


def find_number(my_list):
        low, high = 0, len(my_list) - 1

        while low < high:
            mid = (low + high) // 2
            print(f'LOOKING AT HIGH: {my_list[high]}')
            print(f'LOOKING AT LOW: {my_list[low]}')
            print(f'LOOKING AT MID: {my_list[mid]}\n')

            # If mid element is greater than the last element, min is in the right half
            if my_list[mid] > my_list[high]:
                low = mid + 1
            else:  # Min is in the left half (or at mid)
                high = mid

        print(f'NUMBER: {my_list[low - 1]}')
        return low  # Low is the index of the minimum element (rotation count)




test_list = [
    2, 5, 9, 12, 15, 18, 22, 25, 28, 31, 35, 38, 41, 44, 48, 51, 54, 58, 61, 64,
    67, 71, 74, 77, 80, 83, 87, 90, 94, 97, 101, 105, 108, 111, 115, 119, 122, 126, 130, 133,
    137, 140, 143, 147, 150, 154, 158, 161, 165, 168, 172, 175, 179, 183, 186, 190, 193, 197, 200, 204,
    208, 211, 215, 218, 222, 225, 229, 233, 237, 240, 244, 248, 251, 255, 259, 263, 266, 270, 274, 277,
    281, 285, 288, 292, 296, 299, 303, 307, 311, 315, 318, 322, 326, 329, 333, 337, 341, 344, 348, 352
]


sorted_lists = {
    0: [1, 2, 3, 4, 5],
    1: [10, 20, 30, 40, 50, 60],
    2: [3, 8, 12, 15, 22],
    3: [-10, -5, 0, 5, 10, 15, 20],
    4: [100, 200, 300, 400, 500, 600, 700, 800],
    5: [7, 14, 21, 28, 35, 42, 49],
    6: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
    7: [99, 150, 202, 305],
    8: [5, 10, 15, 25, 35, 45, 55, 65, 75],
    9: [-50, -40, -30, -20, -10, 0, 10, 20]
}

rand_rotation = random.randint(1, 10)
rand_list = random.randint(0, 9)
print(f'Original List: {sorted_lists[rand_list]}')

rotated_list = shift_my_list(sorted_lists[rand_list], rand_rotation)



print(f'Rotated List: {rotated_list}')

# SOLUTION

# Linear Searching O(N), good for unsorted data
# last_number = max(rotated_list)

# index = rotated_list.index(last_number)
# print(index+1)

# print(binary_search(test_list, 22))

print(find_number(rotated_list))




