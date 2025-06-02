
"""

students = [

]

"""

#输入学生数量并依次添加学生姓名到students列表中








def add_student_name(students,input_num_1):
    for input_num in range(input_num_1):
        add_student_name = input("请输入{}个学生的姓名： ".format(input_num + 1))
        students[input_num] [0]= add_student_name
        if input_num == input_num_1-1:
            print("学生信息添加成功！")
            return 0


