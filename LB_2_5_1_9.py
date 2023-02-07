br_date = '19991229'


def didgit_of_life(line):
    num = 0
    for n in line:
        num += int(n)

    if num > 10:
        num2 = 0
        for m in str(num):
            num2 += int(m)

        num = num2
        return str(num)
    else:
        return str(num)

print(didgit_of_life(br_date))
