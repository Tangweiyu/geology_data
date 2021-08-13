s = []
f  = open('txt_floder/all.txt','r',encoding='utf-8')
for lines in f:
    # query_list.append(line.replace('/','').replace('、','').replace(' ','').strip('\n'))
    ls = lines.strip('\n').replace(' ','').replace('、','/').replace('?','').split('/')
    for i in ls:
        s.append(i)
# lines = f.read()
# ls = lines.replace('。', '。\n')
# for i in ls:
#     s.append(i)
f.close()
# print(s)

f1 = open('txt_floder/all_cut_juhao.txt','w',encoding='utf-8')
for j in s:
    f1.write(j+'\n')
f1.close()