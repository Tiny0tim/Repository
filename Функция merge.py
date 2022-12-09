def sort_choice(a):
    n = len(a)
    for i in range(n):
        maximum = max(a[:n - i])
        q = a.index(maximum)
        z = (n - 1) - i
        a[q], a[z] = a[z], a[q]
    return a


def merge(list1, list2):
    t = list1 + list2
    q = sort_choice(t)
    return q


def spisok_chisel_iz_stroki():
    return [int(i) for i in input().split()]


list1 = spisok_chisel_iz_stroki()
list2 = spisok_chisel_iz_stroki()

print(merge(list1, list2))

print("send nudes")

