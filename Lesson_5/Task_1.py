with open("text_1.txt", 'w', encoding="utf-8") as f_obj:
    try:
        while f_obj.write(input("Type something: ")):
            f_obj.write("\n")
    except IOError:
        print("Error!")
