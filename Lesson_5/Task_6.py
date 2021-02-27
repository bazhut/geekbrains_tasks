with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    my_el = {el[0].removesuffix(':'): el[1:] for el in [el.split() for el in f_obj.readlines()]}
    print(my_el)
    for el in my_el.items():
        r = el[1]
        i = 0
        val = []
        while i != len(r):
            temp_val = []
            for a in r[i]:
                if a.isdigit():
                    temp_val.append(a)
            if temp_val:
                val.append(''.join(temp_val))
            i += 1
        val = [int(i) for i in val]
        sum_val = sum(val)
        my_el[el[0]] = sum_val
    print(my_el)
