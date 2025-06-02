


"""

students = [

]

"""

#输入学生数量并依次添加学生成绩到students列表中
def add_student_grade(students,input_num_1,input_num_2):
    for i in range(input_num_1):  # 遍历每个学生
        print("姓名： {}".format(students[i][0]))
        for j in range(2, input_num_2 * 2 + 2, 2):  # 遍历每个学科的成绩位置
            subject_name = students[i][j-1]  # 获取学科名称
            score = float(input("请输入{}的{}成绩： ".format(students[i][0], subject_name)))
            students[i][j] = score  # 存储成绩
        print()  # 每个学生录入完成后换行




#得全部删除，重新做
"""
def add_student_grade(students,input_num_1,input_num_2):
    for subject in range(input_num_2):
        for i in range(input_num_1):
            print("姓名： {}".format(students[i][0]))
            for j in range(2,input_num_2 + 2,2):
                students[i][j] = float(input("请输入{}的{}成绩： ".format(students[i][0],students[i][j-1])))
"""


