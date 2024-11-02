# fileIn = open('input1b.txt', 'r')
# fileOut = open('output1b.txt', 'w')
# lines = fileIn.readline()
# x = fileIn.readline().split()
# print(x)

# print(lines[2])
# for i in range(1, len(lines)):
#     # print(lines[i].split())
#     for j in range(1, len(lines[i].split())):
#         # print(True)
#         if lines[i].split()[j+1] == '+':
#             fileOut.writelines(f'The result of {lines[i][9:]} is {int(lines[i].split()[j]) + int(lines[i].split()[j+2])}\n')
#             break
#         elif lines[i].split()[j+1] == '/':
#             fileOut.writelines(f'The result of {lines[i][9:]} is {int(lines[i].split()[j]) / int(lines[i].split()[j + 2])}\n')
#             break
#         elif lines[i].split()[j+1] == '-':
#             fileOut.writelines(f'The result of {lines[i][9:]} is {int(lines[i].split()[j]) - int(lines[i].split()[j + 2])}\n')
#             break
#         elif lines[i].split()[j+1] == '*':
#             fileOut.writelines(f'The result of {lines[i][9:]} is {int(lines[i].split()[j]) * int(lines[i].split()[j + 2])}\n')
#             break
# for i in range(5):
#     line = fileIn.readline().split()
#     print(line)
with open('input1b.txt', 'r') as fileIn:
    with open('output1b.txt', 'w') as fileOut:
        n = int(fileIn.readline())
        for i in range(n):
            line = fileIn.readline().split()
            if line[2] == '+':
                result = int(line[1]) + int(line[3])
            elif line[2] == '/':
                result = int(line[1]) / int(line[3])
            elif line[2] == '-':
                result = int(line[1]) - int(line[3])
            else:
                result = int(line[1]) * int(line[3])
            fileOut.writelines(f'The result of {line[1]} {line[2]} {line[3]} is {result}\n')