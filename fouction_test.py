"""
用于测试函数的使用方法
"""

# str = '12345667'
#
# result = str.find('1')
# result2 = str.find('8')
# #
# # print(result, result2)
#
#
# list1 = [1, 3]
#
# list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 01234 56789 101121314
# list3 = []
# # print(list2[0:5])
#
#
# i = 0
# a = 0
# # print(list2[a:a+5])
#
# for item in list1:
#     attr1 = list2[a:a+5]
#     list3.append(attr1)
#     print(list3)
#     i += 5
#     a = a + i

# print(list_temp)

list4 = [['Band 1    343.141968   3172.036865   1396.947908   517.576131',
  'Band 2    469.358368   6094.756836   2812.901207  1024.031139',
  'Band 3   1178.856934  16537.927734   7702.931803  2853.871846',
  'Band 4    501.486633   7245.279297   2947.598069  1231.295473',
  'Band 5    941.643677  13906.984375   6609.767779  2447.462605'],['Band 1    343.141968   3172.036865   1396.947908   517.576131',
  'Band 2    469.358368   6094.756836   2812.901207  1024.031139',
  'Band 3   1178.856934  16537.927734   7702.931803  2853.871846',
  'Band 4    501.486633   7245.279297   2947.598069  1231.295473',
  'Band 5    941.643677  13906.984375   6609.767779  2447.462605'],['Band 1    343.141968   3172.036865   1396.947908   517.576131',
  'Band 2    469.358368   6094.756836   2812.901207  1024.031139',
  'Band 3   1178.856934  16537.927734   7702.931803  2853.871846',
  'Band 4    501.486633   7245.279297   2947.598069  1231.295473',
  'Band 5    941.643677  13906.984375   6609.767779  2447.462605'],['Band 1    343.141968   3172.036865   1396.947908   517.576131',
  'Band 2    469.358368   6094.756836   2812.901207  1024.031139',
  'Band 3   1178.856934  16537.927734   7702.931803  2853.871846',
  'Band 4    501.486633   7245.279297   2947.598069  1231.295473',
  'Band 5    941.643677  13906.984375   6609.767779  2447.462605'],['Band 1    343.141968   3172.036865   1396.947908   517.576131',
  'Band 2    469.358368   6094.756836   2812.901207  1024.031139',
  'Band 3   1178.856934  16537.927734   7702.931803  2853.871846',
  'Band 4    501.486633   7245.279297   2947.598069  1231.295473',
  'Band 5    941.643677  13906.984375   6609.767779  2447.462605'],['Band 1    343.141968   3172.036865   1396.947908   517.576131',
  'Band 2    469.358368   6094.756836   2812.901207  1024.031139',
  'Band 3   1178.856934  16537.927734   7702.931803  2853.871846',
  'Band 4    501.486633   7245.279297   2947.598069  1231.295473',
  'Band 5    941.643677  13906.984375   6609.767779  2447.462605']]
def convert_data(list):
    data_list = []
    for sub_list in list:
        list_temp_1 = []

        for item in sub_list:
            str_temp = item[6:].strip()
            list_temp_1.append(str_temp)
            # print(listtemp_1)
        list_temp_2 = '  '.join(list_temp_1)
        list_temp_3 = list_temp_2.split('  ')
        # print(list_temp_3)
        list_temp_4 = []

        for item in list_temp_3:
            new_str = item.strip()
            list_temp_4.append(new_str)
            # print(list_temp_4)

        data_list.append(list_temp_4)
    return  data_list
print(convert_data(list4))






# print(list8)

# list5.append(str1)
# print(list5)