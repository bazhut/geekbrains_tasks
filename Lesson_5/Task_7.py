import json


with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    companies = [el.split() for el in f_obj.readlines()]
    prof_comp = {el[0]: int(el[2]) - int(el[3]) for el in companies}
    prof_ave_list = [el for el in prof_comp.values() if el > 0]
    prof_ave = {"average_profit": (sum(prof_ave_list) / len(prof_ave_list))}
    result = [prof_comp, prof_ave]
    with open("text_71.json", "w", encoding="utf-8") as w_obj:
        json.dump(result, w_obj, ensure_ascii=False, indent=4)
