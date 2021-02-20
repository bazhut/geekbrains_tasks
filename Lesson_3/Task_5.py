def my_func():
    num_list_gl = []
    while True:
        try:
            num = input("Type a numbers or press 'Q': ").upper().split()
            num_list_loc = []
            for i in num:
                if i.isdigit():
                    num_list_loc.append(float(i))
                elif i == "Q":
                    num_list_gl.extend(num_list_loc)
                    return print(f"Local: {sum(num_list_loc)}, Global: {sum(num_list_gl)}")
                else:
                    print("Type only number!")
                    num_list_loc.clear()
                    break
            num_list_gl.extend(num_list_loc)
            print(f"Local: {sum(num_list_loc)}, Global: {sum(num_list_gl)}")
        except ValueError:
            print(f"Type a number!")


my_func()
