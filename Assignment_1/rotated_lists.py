def shift_my_list(my_list, rotate: int = 1) -> list:
    """
    Rotates list last number to index 0
    :param my_list: list to be rotated
    :param rotate: number of times the list in being rotated. I cannot be a higher number than list length.
    :return: Returns rotated list.
    """
    # Number of rotations cannot be higher than list length
    if rotate > len(my_list):
        rotate = len(my_list)

    for x in range(rotate):

        print(f'LAST ELEMENT: {my_list[- 1]}')
        my_list.insert(0, my_list[- 1])

        print(f'LIST: {my_list}, DELETE ELEMENT: {my_list[- 1]}')
        del my_list[- 1]
        print(f'UPDATED LIST: {my_list}')

        print(f'Rotation: {x + 1}\n')

    return my_list


my_sorted_list = [3, 5, 6, 7, 8, 10, 12, 15, 19, 22]

last_number = my_sorted_list[-1]
rotated_list = shift_my_list(my_sorted_list, 3)

print(rotated_list)

# SOLUTION

last_index = sorted(rotated_list)
last_item = last_index[-1]



