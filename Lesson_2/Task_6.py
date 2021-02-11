goods_list = [(1, {'Name': 'q', 'Price': 1, 'Quantity': 2, 'Unit': 'd'}),
              (2, {'Name': 'w', 'Price': 3, 'Quantity': 5, 'Unit': 't'}),
              (3, {'Name': 'h', 'Price': 6, 'Quantity': 4, 'Unit': 'd'}),
              (4, {'Name': 'l', 'Price': 9, 'Quantity': 1, 'Unit': 't'})]
analytics = [{'Name': 'q', 'Price': 1, 'Quantity': 2, 'Unit': 'd'},
             {'Name': 'w', 'Price': 3, 'Quantity': 5, 'Unit': 't'},
             {'Name': 'h', 'Price': 6, 'Quantity': 4, 'Unit': 'd'},
             {'Name': 'l', 'Price': 9, 'Quantity': 1, 'Unit': 't'}]
i = 1
while True:
    answer = input("Do you want to add good? (Yes or No): ").upper()
    if answer == "YES":
        name = input("Name: ")
        price = int(input("Price: "))
        quantity = int(input("Quantity: "))
        unit = input("Unit: ")
        good_dict = {"Name": name, "Price": price, "Quantity": quantity, "Unit": unit}
        goods_list.append((i, good_dict))
        analytics.append(good_dict)
        i += 1
    elif answer == "NO":
        while True:
            analytics_answer = input('Do you want to see analytics?: ').upper()
            if analytics_answer == 'YES':
                n = []
                p = []
                q = []
                u = []
                # type_ = input('Type name, price, quantity or unit: ').title()
                for a in range(len(analytics)):
                    # n.append(analytics[a].get(type_))
                    n.append(analytics[a].get("Name"))
                    p.append(analytics[a].get("Price"))
                    q.append(analytics[a].get("Quantity"))
                    u.append(analytics[a].get("Unit"))
                a_dict = {"Name": n, "Price": p, "Quantity": q, "Unit": u}
                print(a_dict)
                # a_dict = {type_: n}
                # print(a_dict)
                break
            elif analytics_answer == 'NO':
                print("Bye!")
                break
            else:
                print("Type Yes or No!")
        break

    else:
        print("Type Yes or No!")
