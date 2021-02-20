from sys import argv

name, par_1, par_2, par_3 = argv

par_1, par_2, par_3 = int(par_1), int(par_2), int(par_3)
result = (par_1 * par_2) + par_3
print(result)
