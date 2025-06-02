from tqdm import tqdm

from Add_student_grade import add_student_grade

from Calculate_average_1 import calculate_average_1

from Output_student_info import output_student_info

from Add_student_name import add_student_name

from Sure_student_info import sure_student_info

from time import sleep

#列表中添加列表，第一个是学生姓名，第二个是该学生的成绩列表


students = [

]


print("在进行操作之前，请先确定学生总数： ")
input_num_1 = int(input("请输入学生总数： "))
input_num_2 = int(input("请输入学科的数量： "))



sure_student_info(students,input_num_1,input_num_2)


for i in tqdm(range(1,2),desc='Processing',colour='green'):
    sleep(0.1)

print("|***********欢迎登录学生成绩管理系统***********|")
print("|***********1.添加学生姓名*********************|")
print("|***********2.录入成绩*************************|")
print("|***********3.计算平均分***********************|")
print("|***********4.输出学生信息*********************|")
print("|***********5.退出系统*************************|")



while True:
    input_num = int(input("请选择您的操作： "))
    if input_num == 1:
        add_student_name(students,input_num_1)
    elif input_num == 2:
        add_student_grade(students,input_num_1,input_num_2)
    elif input_num == 3:
        calculate_average_1(students,input_num_2)
    elif input_num == 4:
        output_student_info(students,input_num_2)
    elif input_num == 5:
        break



#遇到困难，不知道是一科成绩还是多科成绩



print("|***********欢迎下次使用学生成绩管理系统*******|")



