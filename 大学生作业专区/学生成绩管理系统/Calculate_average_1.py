"""

students = [

]

"""


#计算学生的平均成绩


#那么这个平均值就分为学生个人平均和全部学生的平均，虽然后者实用性不大

def calculate_average_1(students,input_num_2):
    if students == [None] or not students:
        return "请先进行学生信息录入"
    else:
        #先计算学生的个人平均分
        for student in students:
            if not student or len(student) < input_num_2 * 2 + 2:
                continue  # 跳过无效的学生数据
                
            sum_score = 0
            valid_scores = 0  # 记录有效成绩数量
            
            for i in range(2, input_num_2 * 2 + 2, 2):
                if i < len(student) and student[i] is not None:
                    try:
                        sum_score += float(student[i])  # 使用float更安全
                        valid_scores += 1
                    except (ValueError, TypeError):
                        continue  # 跳过无法转换的数据
            
            if valid_scores > 0:
                student_average = sum_score / valid_scores
                student.append("学生的个人平均分： ")
                student.append(student_average)
        
        #计算班级平均分
        total_score = 0
        valid_students = 0
        
        for student in students:
            if len(student) >= 2 and student[-1] is not None:
                try:
                    total_score += float(student[-1])
                    valid_students += 1
                except (ValueError, TypeError):
                    continue
        
        if valid_students > 0:
            students_average = total_score / valid_students
            print("班级平均分：", students_average)
            return "班级平均分： " + str(students_average)
        else:
            return "没有有效的学生成绩数据"






"""
def calculate_average_1(students,input_num_1,input_num_2):
    if students == [None]:
        return "请先进行学生信息录入"
    else:
        #先计算学生的个人平均分
        for student in students:
            sum_socre = 0
            for i in range(2,input_num_2 * 2 + 2,2):
                sum_socre += int( student[i] )
            student_average = sum_socre / (input_num_2)
            student.append("学生的个人平均分： ")
            student.append(student_average)
        

        #计算班级平均分
        sum_socre_1 = 0
        sum_socre_1 = int( student[-1] ) * input_num_1
        students_average = sum_socre_1 / input_num_1
        return "班级平均分： " + str( students_average )











"""