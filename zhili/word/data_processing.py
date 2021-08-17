#coding=utf-8
import docx2txt
import os

def get_all_path(open_file_path):
    rootdir = open_file_path
    path_list = []
    list = os.listdir(rootdir)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        com_path = os.path.join(rootdir, list[i])
        #print(com_path)
        if os.path.isfile(com_path):
            path_list.append(com_path)
        if os.path.isdir(com_path):
            path_list.extend(get_all_path(com_path))
    #print(path_list)
    return path_list


def docx_txt(path_list,txt_save_path):
    for path in path_list:
        file_type = os.path.splitext(path)[-1]
        if file_type == '.docx':
            txt_save_name = str(os.path.join(txt_save_path, os.path.basename(path)))[:-4] + 'txt'
            text = docx2txt.process(path)
            file = open(txt_save_name, 'w', encoding='utf-8')
            file.write(text)
            file.close()
            print(txt_save_name + "——文件保存成功")


#判断输入的存储文件路径是否存在，若不存在则创建
def judge_path(File_Path):
    if not os.path.exists(File_Path):
        os.makedirs(File_Path)
    return File_Path


def docx_to_txt(open_file_path, txt_save_path):
    path_list = get_all_path(open_file_path)
    txt_save_path_exists = judge_path(txt_save_path)
    docx_txt(path_list, txt_save_path_exists)


def txt_together(open_file_path, all_txt_path):
    path_list = get_all_path(open_file_path)
    all_txt_path_exists = judge_path(all_txt_path)
    all_f = open(os.path.join(all_txt_path_exists,'all_txt.txt'),'a',encoding='utf-8')
    for path in path_list:
        single_f = open(path,'r',encoding='utf-8')
        single_txt = single_f.read()
        single_f.close()
        all_f.write(single_txt)
    all_f.close()

if __name__ == '__main__':
    get_all_path(r'data')
    docx_txt(r'data/docx_floder',r'data/txt_floder/method_2')
    judge_path(r'data')
    docx_to_txt(r'data/docx_floder',r'data/txt_floder/method_2')
    # txt_together(r'data/txt_floder/method_2',r'data/txt_floder/method_2')