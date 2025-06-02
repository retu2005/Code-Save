
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
#根据用户输入的课程编号和任课教师，从集合中删除对应的课程

"""
由于之前就用的列表，所以这次依旧用列表来完成
"""


from time import sleep

def delete_curriculum(curriculum_management_systems):
    print("请输入课程编号和任课老师删除对应的课程信息。")
    sleep(1)
    input_num_1 = input("请输入课程编号： ")
    input_num_2 = input("请输入任课老师： ")
    for curriculum_management_system in curriculum_management_systems:
        if input_num_1 == curriculum_management_system['curriculum_id'] and input_num_2 == curriculum_management_system['teacher']:
            del curriculum_management_system
    

    print("删除课程成功！")






