import os
import shutil
import win32com.client as wc
from tqdm import tqdm

if __name__ == '__main__':
    root = os.getcwd()
    # 路径
    file_dir = os.path.join(root, "data")
    ori_file_dir = os.path.join(file_dir, "原数据")    #数据原路径
    docx_file_dir = os.path.join(file_dir, "docx_floder")   #转化完毕后保存的新路径

    if os.path.exists(docx_file_dir): shutil.rmtree(docx_file_dir)
    os.makedirs(docx_file_dir)

    files = os.listdir(ori_file_dir)

    for file_name in tqdm(files):
        ori_file_path = os.path.join(ori_file_dir, file_name)
        if file_name.endswith("docx"):
            target_name = file_name
            target_file_path = os.path.join(docx_file_dir, target_name)
            shutil.copyfile(ori_file_path, target_file_path)
        elif file_name.endswith(".doc"):
            target_name = file_name + "x"
            target_file_path = os.path.join(docx_file_dir, target_name)
            # doc文件另存为docx
            word = wc.Dispatch("Word.Application")
            doc = word.Documents.Open(ori_file_path)
            doc.SaveAs(target_file_path, 12, False, "", True, "", False, False, False, False)
            doc.Close
            word.Quit