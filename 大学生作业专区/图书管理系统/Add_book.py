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

def add_book(books):
    book_id = int(input("Please enter the book_id: "))
    book_name = input("Please enter the book_name: ")
    author = input("Please enter the author: ")
    book_year = int(input("Please enter the book_year: "))
    publisher = input("Please enter the publisher: ")

    new_book = {'book_id':book_id,'book_name':book_name,\
                'author':author,'book_year':book_year,'publisher':publisher}
    books.append(new_book)
    len_for = 0   #len_for 是循环次数，方便判断
    lens = len(books)
    for book in books:
        len_for +=1
        if book == new_book and len_for < lens:
            print("这本书已经存在，请输入其他书籍！")
            del new_book
    print("添加成功！")







