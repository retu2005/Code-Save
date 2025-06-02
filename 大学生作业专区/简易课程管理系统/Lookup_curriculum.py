
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

#输入课程编号  查询课程  


def lookup_curriculum(curriculum_management_systems):
    while True:
        input_print = input("请输入课程编号，查询课程： ")
        for curriculum_management_system in curriculum_management_systems:
            if curriculum_management_system['curriculum_id'] == input_print:
                print("课程编号： {}, 课程名称： {}, 上课教师：{}, 上课时间：{} "\
                        .format(curriculum_management_system['curriculum_id'],\
                        curriculum_management_system['curriculum_name'],\
                        curriculum_management_system['teacher'],\
                        curriculum_management_system['curriculum_time']))

        input_next = input("是否继续查询课程(y(enter)/n)：")
        if input_next == 'y' or input_next == 'Y' or input_next == '':
            lookup_curriculum(curriculum_management_systems)
            return
        if input_next == 'n' or input_next == 'N':
            break


#下面是原来的bug，留作参考

"""
    input_print = input("请输入课程编号，查询课程： ")
    for curriculum_management_system in curriculum_management_systems:
        if curriculum_management_system['curriculum_id'] == input_print:
            print("课程编号： {}, 课程名称： {}, 上课教师：{}, 上课时间：{} "\
                    .format(curriculum_management_system['curriculum_id'],\
                    curriculum_management_system['curriculum_name'],\
                    curriculum_management_system['teacher'],\
                    curriculum_management_system['curriculum_time']))
            



        input_next = input("是否继续查询课程(y(enter)/n)：")
        if input_next == 'y' or input_next == 'Y' or input_next == '':
            lookup_curriculum(curriculum_management_systems)
            return
        if input_next == 'n' or input_next == 'N':
            break
"""