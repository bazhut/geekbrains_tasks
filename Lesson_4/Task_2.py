list_ = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_new = [list_[num] for num in range(1, len(list_)) if list_[num] > list_[num - 1]]
print(list_new)
