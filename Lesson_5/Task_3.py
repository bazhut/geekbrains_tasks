from statistics import mean


with open("text_3.txt", "r", encoding="utf-8") as f_obj:
    my_dict = {el.split()[0]: float(el.split()[1]) for el in f_obj}
    print("Сотрудники с зарплатой менее 20к:")
    for i in my_dict.items():
        if i[1] < 20000:
            print(i[0])
    salary_list = [el for el in my_dict.values()]
    print(f"Средняя зарплата сотрудников: {mean(salary_list)} р.")
