my_translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", "r") as f_obj:
    list_ = [i.split() for i in f_obj.readlines()]
    for i in list_:
        i[0] = my_translate.get(i[0])
    list_translate = [' '.join(el) for el in list_]
    with open("text_4_translate.txt", "w", encoding="utf-8") as f_obj_translate:
        for i in list_translate:
            f_obj_translate.write(f"{i}\n")
