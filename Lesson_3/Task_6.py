def int_func(text):
    try:
        back_list_gl = []
        text = text.split()
        while True:
            for k in text:
                back_list_loc = []
                for i in k:
                    i = ord(i)
                    if 97 <= i <= 122:
                        i = chr(i)
                        back_list_loc.append(i)
                    else:
                        back_list_loc.clear()
                        break
                if back_list_loc:
                    back_list_loc.append(" ")
                    back_list_loc[0] = back_list_loc[0].upper()
                    back_list_gl.extend(back_list_loc)
            if back_list_gl:
                back_list_gl.pop(-1)
            result = " ".join(back_list_gl)
            break
        return result
    except AttributeError:
        print("Atr must be str!")


print(int_func("dkjhibhib incoiuashc jns8jbn"))

