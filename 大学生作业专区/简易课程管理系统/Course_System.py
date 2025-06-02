#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#简易课程管理系统
from Print_curriculum import print_curriculum

from Add_curriculum import add_curriculum

from Lookup_curriculum import lookup_curriculum

from Delete_curriculum import delete_curriculum

from Print_print import print_print
"""
1.选取合适的组合数据类型存储课程信息和集合，每个课程信息包含curriculum_id'、curriculum_name、teacher和curriculum_time。
"""
#选择str 

curriculum_management_systems = [
    {'curriculum_id':'LX190020','curriculum_name':'概率论与数理统计',\
        'teacher':'丁','curriculum_time':'星期三第一讲'},

    {'curriculum_id':'LX240170','curriculum_name':'Python程序设计及应用SL',\
        'teacher':'徐','curriculum_time':'星期一第五讲'},

    {'curriculum_id':'LX240170','curriculum_name':'Python程序设计及应用SL',\
        'teacher':'马','curriculum_time':'星期二第二讲'},

    {'curriculum_id':'LX240260','curriculum_name':'数学建模SL',\
        'teacher':'杨','curriculum_time':'星期五第四讲'},

]
print_print()

while True:
    input_num = int(input("请选择您想要的操作（输入6可以查看操作信息）："))
    if input_num == 1:
        print_curriculum(curriculum_management_systems)
    elif input_num == 2:
        add_curriculum(curriculum_management_systems)
    elif input_num == 3:
        lookup_curriculum(curriculum_management_systems)
    elif input_num == 4:
        delete_curriculum(curriculum_management_systems)
    elif input_num == 5:
        print("|************欢迎下次使用！*******************|")
        break
    if input_num == 6:
        print_print()











