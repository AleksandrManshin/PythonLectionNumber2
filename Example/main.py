# with open('file.txt', 'a') as data:
#     data.write('line 2222\n')
#     data.write('line 1111\n')


# colors = ['red', 'green', 'blue']
# data = open ('file.txt', 'a')
# data.writelines(colors)
# data.write('\nLINE2\n')
# data.close

# path = 'file.txt'
# data = open (path, 'r')
# for line in data:
#     print(line)
# data.close

# def f(x):
#     if x == 1:
#         return 'Целое'
#     elif x == 2.3:
#         return 23
#     else:
#         return

# def concatenatio(*params):
#     res: str = ""
#     for item in params:
#         res += item
#     return res

# print(concatenatio('a', 's', 'd', 'w'))
# print(concatenatio('a', '1'))

# a = (3, 4)
# print(a[-1])

# for item in a:
#     print(item)


dictionary = {}
dictionary = \
 {
 'up': '↑',
 'left': '←',
 'down': '↓',
 'right': '→'
 }
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left'])

for k in dictionary.values():
    print(k)