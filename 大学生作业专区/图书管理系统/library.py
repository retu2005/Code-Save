from Add_book import *
from Lookup_book import *
from Modify_book import *
from Delete_book import *
"""
图书管理系统
"""
#encoding='utf-8'

#数据类型  int string

# 创建一个字典，方便存储图书信息

books = [
    {'book_id':9787302663799,'book_name':'python程序设计',\
        'author':'董付国','book_year':2025,'publisher':'清华大学出版社'},
    {'book_id':9787030673206,'book_name':'应用多元统计分析',\
        'author':'李建平','book_year':2021,'publisher':'科学出版社'},
    {'book_id':9787040629637,'book_name':'数学模型',\
        'author':'姜启源','book_year':2024,'publisher':'高教出版社'},
    {'book_id':9787111632023,'book_name':'机器学习及其应用',\
        'author':'汪荣贵','book_year':2019,'publisher':'机械工业出版社'},  
    
]

print("|********欢迎登录图书管理系统************|")
print("|********1.添加图书**********************|")
print("|********2.查询图书**********************|")
print("|********3.修改图书信息******************|")
print("|********4.删除图书**********************|")
print("|********5.打印所有图书信息**************|")


while True:
    input_num = int(input("请输入操作序号："))

    if input_num == 1:
        add_book(books)
    elif input_num == 2:
        lookup_book(books)
    elif input_num == 3:
        modify_book(books)
    elif input_num == 4:
        delete_book(books)
    elif input_num == 5:
        for book in books:
            print(book)
    else:
        print("输入错误，请重新输入！")
    input_num_quit = input("是否退出系统？(y(enter)/n): ")
    if input_num_quit == 'y' or input_num_quit == 'Y' or input_num_quit == '':
        break
    else:
        continue

print("|*********欢迎下次使用图书管理系统*******|")












