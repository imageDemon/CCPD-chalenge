# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 下午3:55
# @Author  : Mat
# @Email   : 735678367@qq.com
# @File    : data_processing.py
# @Software: PyCharm
from PIL import Image
import os
path = '/apps/ccpd_challenge/'
save_path = '/apps/ccpd_challenge_processing_label/'
filelist = os.listdir(path)
print len(filelist)
if os.path.exists(save_path) is False:
    os.mkdir(save_path)

#print filelist[0]
provinces = ["皖", "沪", "津", "渝", "冀", "晋",
             "蒙", "辽", "吉", "黑", "苏", "浙",
             "京", "闽", "赣", "鲁", "豫", "鄂",
             "湘", "粤", "桂", "琼", "川", "贵",
             "云", "藏", "陕", "甘", "青", "宁",
             "新", "警", "学", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'J', 'K', 'L', 'M',
             'N', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
       'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R',
       'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
       '0', '1', '2', '3', '4', '5', '6', '7',
       '8', '9', 'O']
num = 0
if os.listdir(save_path)==[]:
    for i in filelist:
        img_id = os.path.join(path, i)
        img = Image.open(img_id)
        strs = img_id.split('-')
        #print strs[3]
        # coordinates
        LP_coord = strs[3]
        LP_coord = LP_coord.split('_')
        print LP_coord
        LP_coord_1 = LP_coord[0].split('&')
        LP_coord_2 = LP_coord[1].split('&')
        LP_coord_3 = LP_coord[2].split('&')
        LP_coord_4 = LP_coord[3].split('&')
        if int(LP_coord_2[0]) < int(LP_coord_3[0]):
            LP_coord_left = int(LP_coord_2[0])
        else:
            LP_coord_left = int(LP_coord_3[0])
        if int(LP_coord_3[1]) < int(LP_coord_4[1]):
            LP_coord_upper = int(LP_coord_3[1])
        else:
            LP_coord_upper = int(LP_coord_4[1])
        if int(LP_coord_1[0]) < int(LP_coord_4[0]):
            LP_coord_right = int(LP_coord_4[0])
        else:
            LP_coord_right = int(LP_coord_1[0])
        if int(LP_coord_1[1]) < int(LP_coord_2[1]):
            LP_coord_lower = int(LP_coord_2[1])
        else:
            LP_coord_lower = int(LP_coord_1[1])
        coord = (int(LP_coord_left), int(LP_coord_upper), int(LP_coord_right), int(LP_coord_lower))
        #print coord
        cropped = img.crop(coord)

        #licence
        LP_number = strs[4]
        print LP_number
        LP_number = LP_number.split('_')
        LP_provinces = provinces[int(LP_number[0])]
        LP_alphabets = alphabets[int(LP_number[1])]
        LP_abs_0 = ads[int(LP_number[2])]
        LP_abs_1 = ads[int(LP_number[3])]
        LP_abs_2 = ads[int(LP_number[4])]
        LP_abs_3 = ads[int(LP_number[5])]
        LP_abs_4 = ads[int(LP_number[6])]
        LP_abs = LP_abs_0 + LP_abs_1 + LP_abs_2 + LP_abs_3 + LP_abs_4

        name = str(num)+'_'+LP_provinces+'-'+LP_alphabets+'-'+LP_abs
        name = str(name) + '.jpg'
        cropped.save(os.path.join(save_path, name))
        num += 1
        # print LP_abs
# img_path = os.path.join(save_path, '149_0-0-826S8.jpg')
# img = Image.open(img_path)
# img.show()
new_file = os.listdir(save_path)
