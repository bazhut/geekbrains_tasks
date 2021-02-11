rating = [8, 9, 1, 4, 2, 1]
rating.sort(reverse=True)
new_rating = int(input("Поставьте оценку от 1 до 10: "))
if new_rating in rating:
    rating.reverse()
    rating.insert(rating.index(new_rating), new_rating)
    rating.reverse()
else:
    rating.append(new_rating)
    rating.sort(reverse=True)
print(rating)
