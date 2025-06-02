
"""
students = [

]

"""

#确认学生数量以及学科数量


def sure_student_info(students,input_num_1,input_num_2):
    for i in range(int(input_num_1)):
        student = [None for j in range(int(input_num_2)  * 2 + 1)]   #用来表示学科和成绩的对应关系，多加的1，表示学生的姓名
        students.append(student)
    print("开始输入学科信息： ")
    for i in range(1,int(input_num_2) * 2 + 1,2):
        student[i] = input("请输入第{}门学科的名称： ".format(i//2 + 1))
        for j in range(int(input_num_1)):
            students[j][i] = student[i]
















