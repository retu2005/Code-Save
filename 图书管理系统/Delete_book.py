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


def delete_book(books):
    account = 0
    input_id = input("Please enter the book_id you want to delete: ")
    for book in books:
        for key,value in book.items():
            if value == int(input_id):
                del books[books.index(book)]
                account += 1

    if account == 0:
        print("您输入的图书编号不存在！")






