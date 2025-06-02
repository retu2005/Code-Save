
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

from time import sleep
#添加课程信息

def add_curriculum(curriculum_management_systems):
    new_curriculum = {}
    print("即将跳转添加课程页面......")
    sleep(1)
    new_curriculum['curriculum_id'] = input("请输入课程编号： ")
    new_curriculum['curriculum_name'] = input("请输入课程名称： ")
    new_curriculum['teacher'] = input("请输入上课教师： ")
    new_curriculum['curriculum_time'] = input("请输入上课时间： ")
    curriculum_management_systems.append(new_curriculum)
    input_next = input("是否继续添加书籍？(y(enter)/n)")
    if input_next == 'y' or input_next == 'Y' or input_next == '':
        add_curriculum(curriculum_management_systems)
        return
    if input_next == 'n' or input_next == 'N':
        return
    

