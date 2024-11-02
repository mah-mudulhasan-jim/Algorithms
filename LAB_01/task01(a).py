# fileIn = open('input1(a).txt', 'r')
# fileOut = open('outputs1(a).txt', 'w')
# lines = fileIn.readlines()
# # print(lines)
# n = int(lines[0].strip())
# for i in range(1, n+1):
#     current = int(lines[i].strip())
#     if current % 2 == 0:
#         # print(f'{current} is an Even number.')
#         fileOut.writelines(str(current) + ' is an Even number.\n')
#     else:
#         fileOut.writelines(str(current) + ' is an Odd number.\n')

with open('input1(a).txt', 'r') as fileIn:
    with open('outputs1(a).txt', 'w') as fileOut:
        lines = fileIn.readlines()
        # print(lines)
        n = int(lines[0].strip())
        for i in range(1, n + 1):
            current = int(lines[i].strip())
            if current % 2 == 0:
                # print(f'{current} is an Even number.')
                fileOut.writelines(str(current) + ' is an Even number.\n')
            else:
                fileOut.writelines(str(current) + ' is an Odd number.\n')

