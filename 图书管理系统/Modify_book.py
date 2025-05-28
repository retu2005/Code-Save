"""
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
"""


def modify_book(books):
    # 输入要修改的书籍的book_id
    book_id = int(input("Please enter the book_id you want to Midify: "))

    for book in books:
        for key, value in book.items():
            if value == book_id:
                print("|***请选择您想修改的信息：**| ")
                print("|****1.book_id************|")
                print("|****2.book_name**********|")
                print("|****3.author*************|")
                print("|****4.book_year**********|")
                print("|****5.publisher**********|")
                print("|***每次输入后请按回车键****|")

                for i in range(5):
                    input_num = input("请输入您想修改的信息序号：")
                    if input_num == '':  #空字符串退出modify_book函数
                        break
                    if int(input_num) == 1:
                        book['book_id'] = int(input("请输入新的book_id："))
                    if int(input_num) == 2:
                        book['book_name'] = input("请输入新的book_name：")
                    if int(input_num) == 3:
                        book['author'] = input("请输入新的author：")
                    if int(input_num) == 4:
                        book['book_year'] = int(input("请输入新的book_year："))
                    if int(input_num) == 5:
                        book['publisher'] = input("请输入新的publisher：")
                    print("修改成功！")
                    print(book)
                    next = input("是否继续修改？(y/n)")
                    if next == 'n':
                        break
                            












