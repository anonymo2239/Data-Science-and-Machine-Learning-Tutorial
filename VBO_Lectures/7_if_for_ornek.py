
salaries = [1000, 2000, 3000, 4000, 5000]
salaries_new = []

def maas_ust(x):
    x = x + (x / 10)
    return x

def maas_alt(x):
    x = x + (x / 5)
    return x

for i in salaries:
    if i < 3000:
        i = maas_alt(i)
        salaries_new.append(i)
    else:
        i = maas_ust(i)
        salaries_new.append(i)

salaries_new.sort()
salaries = salaries_new
print(salaries)
