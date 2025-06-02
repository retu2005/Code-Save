

"""
curriculum_management_system = [
    {'curriculum_id':'LX190020','curriculum_name':'概率论与数理统计',\
        'teacher':'丁','curriculum_time':'星期三第一讲'},

    {'curriculum_id':'LX240170','curriculum_name':'Python程序设计及应用SL',\
        'teacher':'徐','curriculum_time':'星期一第五讲'},

    {'curriculum_id':'LX240170','curriculum_name':'Python程序设计及应用SL',\
        'teacher':'马','curriculum_time':'星期二第二讲'},

    {'curriculum_id':'LX240260','curriculum_name':'数学建模SL',\
        'teacher':'杨','curriculum_time':'星期五第四讲'},

]
"""


#查看课程信息

def print_curriculum(curriculum_management_systems):
    for curriculum_managemengt_system in curriculum_management_systems:
        print("课程编号：{}, 课程名称： {}, 教师： {}, 上课时间： {}".\
                format(curriculum_managemengt_system['curriculum_id'],\
                curriculum_managemengt_system['curriculum_name'],\
                curriculum_managemengt_system['teacher'],\
                curriculum_managemengt_system['curriculum_time']))