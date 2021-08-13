import os
# 打开写入文件
file = open('all.txt', 'a', True, encoding='utf-8')
# 获取当前路径
pwd = os.getcwd()
# 随机遍历读取目录中的文件
files = os.walk(pwd)

for path, dir_list, file_list in files:
    # 遍历List中的文件
    for file_name in file_list:
        # 根据文件名称进行过滤
        if file_name[0] == '1':
            # print(file_name)
            # 打开读取文件
            f = open(file_name,'r',True,encoding='utf-8')
            # 按行遍历读取文件
            for line in f:
                # 写入文件
                file.write(line)
            # 关闭读取流
            f.close()
    # 关闭写入流
    file.close()


# # -*- coding:utf-8*-
# import sys
# from imp import reload
#
# reload(sys)
# sys.setdefaultencoding('utf-8')
# import os
# import os.path
# import time
# time1=time.time()
# ##########################合并同一个文件夹下多个txt################
# def MergeTxt(filepath,outfile):
#   k = open(filepath+outfile, 'a+')
#   for parent, dirnames, filenames in os.walk(filepath):
#     for filepath in filenames:
#       txtPath = os.path.join(parent, filepath) # txtpath就是所有文件夹的路径
#       f = open(txtPath)
#       ##########换行写入##################
#       k.write(f.read()+"\n")
#   k.close()
#   print("finished")
# if __name__ == '__main__':
#   filepath="D:/Workspace/Pycharm workspace/hykj/zhili/word/data/txt_floder"
#   outfile="result.txt"
#   MergeTxt(filepath,outfile)
#   time2 = time.time()
#   print(u'总共耗时：' + str(time2 - time1) + 's')
#

