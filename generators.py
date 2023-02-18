# 1
# print([i * i for i in range(1, int(input()) + 1)])

# 2
# print([i * i for i in range(1, int(input()) + 1) if i % 2 == 0])

# 3
# def iterate(s):
#     for i in range(len(s)):
#         if i % 3 == 0 and i % 4 == 0:
#             print(i, end=' ')
#
#
# s = [i for i in range(0, int(input()) + 1)]
# iterate(s)


# 4
# def sq(a, b):
#     squares = [i ** 2 for i in range(a, b + 1)]
#     for i in squares:
#         yield i
#
#
# a, b = int(input()), int(input())
# sqq = sq(a, b)
# for i in sqq:
#     print(i, end=' ')

# 5
# print([i for i in range(int(input()), -1, -1)])