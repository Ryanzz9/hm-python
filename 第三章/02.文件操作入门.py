# 读文件
from openai.resources.skills import content

# 1.打开文件
f = open("resources/wlspb.txt","r",encoding="utf-8")


# 2.读取文件内容

# content = f.read() # 读取所有内容
# print(content)


content_list = f.readlines()

for line in content_list:
    print(line.strip())


# 3.关闭文件
f.close()



# 写文件

f = open("resources/静夜思.txt","w",encoding="utf-8")  \

# 2.写入文件

f.write("静夜思(李白)\n")
f.write("窗前明月光，\n")
f.write("疑是地上霜。\n")
f.write("举头望明月，\n")
f.write("低头思故乡。\n")

# 3.关闭文件
f.close()