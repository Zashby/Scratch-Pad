def something(n):
    try:
        return int(not sum([1 for x in list(('{:032b}'.format(n))) if x=='1']) % 2 ==0)
    except:
        return -1


print(something(8))

print(something('n'))

print(something(True))