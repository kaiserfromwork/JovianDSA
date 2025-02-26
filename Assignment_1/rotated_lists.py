import random


def shift_my_list(my_list, rotate: int = 1) -> list:
    """
    Rotates list last number to index 0
    :param my_list: list to be rotated
    :param rotate: number of times the list in being rotated. I cannot be a higher number than list length.
    :return: Returns rotated list.
    """
    # Number of rotations cannot be higher than list length
    if rotate >= len(my_list):
        rotate = len(my_list) - 1

    for x in range(rotate):
        my_list.insert(0, my_list[- 1])
        del my_list[- 1]

    return my_list


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
last_number = max(rotated_list)
index = rotated_list.index(last_number)

print(index+1)




