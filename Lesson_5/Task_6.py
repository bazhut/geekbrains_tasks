with open("text_6.txt", "r", encoding="utf-8") as f_obj:
    my_list = [el for el in f_obj.readlines()]
    for i in my_list:
        print(i)
    print(my_list)
