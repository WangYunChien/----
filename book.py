class Book():
    def __init__(self, name, author, publish, year):
        self.name = name 
        self.author = author 
        self.publish = publish 
        self.year = year 

    def info(self):
        return "書名：{}\n作者：{}\n出版社：{}\n年份：{}\n".format(self.name, self.author, self.publish, self.year)
