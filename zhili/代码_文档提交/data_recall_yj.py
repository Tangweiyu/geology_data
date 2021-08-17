# coding = utf-8

from docx import Document
import re
# import cpca
import os
import pandas as pd
from pandas.core.frame import DataFrame

import json



def list_dir(file_dir):
    '''
        通过 listdir 得到的是仅当前路径下的文件名，不包括子目录中的文件，如果需要得到所有文件需要递归
    '''
    # print('\n\n<><><><><><> listdir <><><><><><>')
    # print( "current dir : {0}".format(file_dir))
    dir_list = os.listdir(file_dir)
    # for cur_file in dir_list:
    #     # 获取文件的绝对路径
    #     path = os.path.join(file_dir, cur_file)
    #     if os.path.isfile(path): # 判断是否是文件还是目录需要用绝对路径
    #         print("{0} : is file!".format(cur_file))
    #     if os.path.isdir(path):
    #         print("{0} : is dir!".format(cur_file))
    #         list_dir(path) # 递归子目录
    return dir_list

# def line_together():
#     dir_name = 'data'
#     file_list = list_dir(dir_name)
#     print(file_list)
#     output = open('origin_yj/origindata.txt', 'w', encoding='utf-8')
#     for file in file_list:
#         if file.endswith('.docx'):
#             doc = Document(os.path.join(dir_name, file))
#             for paragraph in doc.paragraphs:
#                 output.write(str(paragraph.text))
#                 output.write('\n')
#     output.close()

def data_recall():
    others_save = open('origin_yj/origindata(1).txt','w',encoding='utf-8')
    # water_type_save = open('origin_yj/水化学类型.txt','w',encoding='utf-8')
    # season_save = open('origin_yj/季节.txt','w',encoding='utf-8')
    # stratigraphic_lithology_save = open('origin_yj/地层岩性.txt','w',encoding='utf-8')
    # wind_direction_save = open('origin_yj/风向.txt','w',encoding='utf-8')
    temperature_save = open('origin_yj/气温.txt','w',encoding='utf-8')
    disaster_name_save = open('origin_yj/灾害名.txt','w',encoding='utf-8')
    density_save = open('origin_yj/密度.txt','w',encoding='utf-8')
    event_name_save = open('origin_yj/事件名.txt','w',encoding='utf-8')
    volume_save = open('origin_yj/体积.txt','w',encoding='utf-8')
    position_save = open('origin_yj/方位.txt','w',encoding='utf-8')
    date_save = open('origin_yj/日期.txt','w',encoding='utf-8')
    meteorology_name_save = open('origin_yj/气象名.txt','w',encoding='utf-8')
    length_save = open('origin_yj/长度.txt','w',encoding='utf-8')
    organization_name_save = open('origin_yj/机构名.txt','w',encoding='utf-8')
    strength_save = open('origin_yj/强度.txt','w',encoding='utf-8')
    acceleration_save = open('origin_yj/加速度.txt','w',encoding='utf-8')
    place_save = open('origin_yj/地点.txt','w',encoding='utf-8')
    climate_save = open('origin_yj/气候.txt','w',encoding='utf-8')
    pH_save = open('origin_yj/pH.txt','w',encoding='utf-8')
    slope_save = open('origin_yj/坡度.txt','w',encoding='utf-8')
    method_save = open('origin_yj/方法.txt','w',encoding='utf-8')
    dip_angle_save = open('origin_yj/倾角.txt','w',encoding='utf-8')
    area_save = open('origin_yj/面积.txt','w',encoding='utf-8')
    level_save = open('origin_yj/级别.txt','w',encoding='utf-8')
    mineralization_degree_save = open('origin_yj/矿化度.txt','w',encoding='utf-8')
    speed_save = open('origin_yj/速度.txt','w',encoding='utf-8')
    file_name_save = open('origin_yj/文件名.txt','w',encoding='utf-8')
    people_result_save = open('origin_yj/人数及受灾情况.txt', 'w', encoding='utf-8')
    economic_loss_save = open('origin_yj/经济损失.txt','w',encoding='utf-8')
    construction_situation_save = open('origin_yj/建筑情况.txt','w',encoding='utf-8')
    farmland_situation_save = open('origin_yj/农田情况.txt','w',encoding='utf-8')
    gushing_water_save = open('origin_yj/涌水量.txt','w',encoding='utf-8')
    rainfall_save = open('origin_yj/降水量.txt','w',encoding='utf-8')
    altitude_save = open('origin_yj/海拔.txt','w',encoding='utf-8')



    with open('origin_yj/origindata.txt','r',encoding='utf-8') as f:
        for line in f.readlines():
            line = line.split()
            line = ''.join(line)
            # if '水化学类型' in line or '水类型' in line:
            #     water_type_save.write(line)
            #     water_type_save.write('\n')
            # elif ('汛期' in line or '雨季' in line or '干旱' in line or
            #     '炎热' in line or '高温' in line) and ('月' in line or '季' in line):
            #     season_save.write(line)
            #     season_save.write('\n')
            # elif '地层岩性' in line or '岩性' in line:
            #     stratigraphic_lithology_save.write(line)
            #     stratigraphic_lithology_save.write('\n')
            # elif ('东' in line or '南' in line or '西' in line or '北' in line) and '风' in line:
            #     wind_direction_save.write(line)
            #     wind_direction_save.write('\n')
            if '°C' in line or '气温' in line or '温度' in line:
                temperature_save.write(line)
                temperature_save.write('\n')
            elif '滑坡' in line or '塌' in line or '泥石流' in line or '水土流失' in line\
                    or '地裂缝' in line or '沉降' in line or '开裂' in line:
                disaster_name_save.write(line)
                disaster_name_save.write('\n')
            elif '密度' in line:
                density_save.write(line)
                density_save.write('\n')
            elif '"' in line:
                event_name_save.write(line)
                event_name_save.write('\n')
            elif 'm3' in line or '体积' in line or 'm³' in line:
                volume_save.write(line)
                volume_save.write('\n')
            elif '东' in line or '南' in line or '西' in line or '北' in line or '方向' in line:
                position_save.write(line)
                position_save.write('\n')
            elif '日' in line:
                date_save.write(line)
                date_save.write('\n')
            elif '雨' in line or '干旱' in line or '大气' in line or '蒸发' in line:
                meteorology_name_save.write(line)
                meteorology_name_save.write('\n')
            elif '长度' in line or '宽度' in line or '厚度' in line or '米' in line or 'm' in line:
                length_save.write(line)
                length_save.write('\n')
            elif '部' in line or '厅' in line or '政府' in line or '国土资源' in line or '院' in line\
                    or '总站' in line or '局' in line or '公安' in line or '安监' in line:
                organization_name_save.write(line)
                organization_name_save.write('\n')
            elif '强度' in line or '严重' in line or '轻微' in line or '强' in line or '弱' in line or '高' in line or '低' in line:
                strength_save.write(line)
                strength_save.write('\n')
            elif '加速度' in line:
                acceleration_save.write(line)
                acceleration_save.write('\n')
            elif '省' in line or '市' in line or '区' in line or '县' in line or '镇' in line or '村' in line:
                place_save.write(line)
                place_save.write('\n')
            elif '气候' in line or '季风' in line:
                climate_save.write(line)
                climate_save.write('\n')
            elif 'pH' in line:
                pH_save.write(line)
                pH_save.write('\n')
            elif '坡度' in line or '°' in line:
                slope_save.write(line)
                slope_save.write('\n')
            elif '采用' in line or '法' in line:
                method_save.write(line)
                method_save.write('\n')
            elif '倾角' in line:
                dip_angle_save.write(line)
                dip_angle_save.write('\n')
            elif '面积' in line or 'm2' in line or '㎡' in line:
                area_save.write(line)
                area_save.write('\n')
            elif '级' in line or '规模' in line:
                level_save.write(line)
                level_save.write('\n')
            elif '矿化度' in line:
                mineralization_degree_save.write(line)
                mineralization_degree_save.write('\n')
            elif '速度' in line:
                speed_save.write(line)
                speed_save.write('\n')
            elif '文件名' in line or '《' in line:
                file_name_save.write(line)
                file_name_save.write('\n')
            elif '死' in line or '农田' in line or '伤' in line \
                    or '毁' in line or '人' in line or '民' in line:
                people_result_save.write(line)
                people_result_save.write('\n')
            elif '元' in line:
                economic_loss_save.write(line)
                economic_loss_save.write('\n')
            elif '房屋' in line or '发电站' in line or '小学' in line or '楼房' in line:
                construction_situation_save.write(line)
                construction_situation_save.write('\n')
            elif '农田' in line:
                farmland_situation_save.write(line)
                farmland_situation_save.write('\n')
            elif '涌水量' in line:
                gushing_water_save.write(line)
                gushing_water_save.write('\n')
            elif '降水量' in line or '雨量' in line or 'mm' in line:
                rainfall_save.write(line)
                rainfall_save.write('\n')
            elif '海拔' in line or '高' in line:
                altitude_save.write(line)
                altitude_save.write('\n')
            else:
                others_save.write(line)
                others_save.write('\n')

    others_save.close()
    altitude_save.close()
    rainfall_save.close()
    gushing_water_save.close()
    farmland_situation_save.close()
    construction_situation_save.close()
    economic_loss_save.close()
    people_result_save.close()
    file_name_save.close()
    speed_save.close()
    mineralization_degree_save.close()
    level_save.close()
    area_save.close()
    dip_angle_save.close()
    method_save.close()
    slope_save.close()
    pH_save.close()
    climate_save.close()
    place_save.close()
    acceleration_save.close()
    strength_save.close()
    organization_name_save.close()
    length_save.close()
    meteorology_name_save.close()
    date_save.close()
    position_save.close()
    volume_save.close()
    event_name_save.close()
    density_save.close()
    disaster_name_save.close()
    temperature_save.close()
    place_save.close()
    # water_type_save.close()
    # season_save.close()
    # stratigraphic_lithology_save.close()
    # wind_direction_save.close()




# def possible_class_static():
#
#     with open('origin_yj/origindata.txt','r',encoding='utf-8') as f:
#         quality = 0
#         for line in f.readlines():
#             if ('汛期' in line or '雨季' in line or '干旱' in line or
#                 '炎热' in line or '高温' in line) and ('月' in line or '季' in line):
#                 quality += 1
#                 print(line)
#         print('沉降量',quality)



if __name__ == '__main__':

    # line_together()
    data_recall()
    # possible_class_static()