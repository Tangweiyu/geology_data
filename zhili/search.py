import re

filepath = "D:/Workspace/Pycharm workspace/hykj/zhili/2018001.txt"

txt = open(filepath, "r", encoding='UTF-8').read()

result=""
test_text = re.findall("{{place+..............+}}", txt)#取出每行含有pass的文本
result = result +'\n'.join(test_text)#换行输出
print(result)