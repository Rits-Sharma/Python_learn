#  Map function is used to apply a function to all the items in an iterable (list, tuple etc.) and return a map object (an iterator).
# a = [1, 2, 3, 4, 5]
# # result = map(lambda x : x**2, a)
# def square(x):
#     return x**2
# result = map(square, a)
# print(list(result))

# Filter function is used to filter the items in an iterable (list, tuple etc.) and return a filter object (an iterator) containing only the items that satisfy the condition.

# def even(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
    
a = [1, 2, 52, 36, 45, -9]
# result = filter(even, a)
result = filter(lambda x : x % 2 != 0, a)

print(list(result))

