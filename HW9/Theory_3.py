number_box_1 = [1, 2, 3]
number_box_2 = [4, 5, 6]
numbers_combined = [n_1 * n_2 for n_1 in number_box_1 for n_2 in number_box_2]
print(numbers_combined)  # [4, 5, 6, 8, 10, 12, 12, 15, 18]
