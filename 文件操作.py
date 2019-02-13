# 1.处理文件，用户指定要查找的文件和内容，将文件中包含要查找内容的每一行都输出到屏幕
def check_file(filename,aim):
    with open(filename,encoding='utf-8') as f:   #句柄 : handler,文件操作符，文件句柄
        for i in f:
            if aim in i:
                yield i

g = check_file('文件.py','django')
for i in g:
    print(i.strip())
print("=========")

#在每行的开头添加
with open("文件.py",encoding='utf-8') as f0:
    for i in f0:
        if 'django' in i:
            # print("====="+i)




#替换
with open("文件.py",'r+',encoding='utf-8') as f0:
    for i in f0:
        if 'django' in i:
            line = i.replace('django','aaaaaaaaaa')
            print(line)
            f0.write(line)

f0.close()
# dir 查看一个变量拥有的方法
print(dir([]))
print(dir(1))
print(dir(list))
