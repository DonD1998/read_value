# 想办法提起特定字符串
import os

input_path = os.path.abspath('test.txt')

# 准备名称列表
# with open(input_path, 'r') as f:
#     file = f.readlines()
#     nameoflist = []


#     for line in file:
#         lineS = line.strip()
#         lineSS = lineS.split('         ')
#         realline = lineSS[0]
#         nameoflist.append(realline)
#     # print(nameoflist)

#     i = 1
#     while i <= 3:
#         nameoflist.pop(0)
#         i += 1

#     print(nameoflist)

# 准备数据列表列表
input_path2 = os.path.abspath('test2.txt')

with open(input_path2, 'r') as f2:
    file_2 = f2.readlines()
    list2 = []
    list2.append('nb')

    for line in file_2:
        lineS = line.strip()
        list2.append(lineS)
        # print(lineS)
    print(list2)
