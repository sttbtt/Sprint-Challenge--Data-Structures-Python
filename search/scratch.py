import math
# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# x = lambda pair: pair[0]
# pairs.sort(key=x)
# print(pairs)


arr = []
cb = lambda x: arr.append(x)

def arr_append(cb):
    for i in range(10):
        cb(i)

arr_append(cb)
print(arr)

square_rt = lambda x: math.sqrt(x)

print(square_rt(64))



