with open("text_1.txt", "r") as f_obj:
    content = f_obj.readlines()
    print(f"Количество строк в файле: {len(content)}")
    words = [len(el.split()) for el in content]
    i = 1
    for el in words:
        print(f"Количество слов в строке {i}: {el}")
        i += 1
