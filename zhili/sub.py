import re
#
# with open(r'代码_文档提交/origin_yj/灾害名.txt', 'r', encoding='utf-8') as f:
#     lines = []
#     for line in f:
#      if line.startswith("滑坡") or line.startswith("泥石流"):
#       split_line = line.split()
#       split_line.insert(split_line.index("滑坡"), "{{disaster_name:")
#       lines.append(' '.join(split_line) + '\n')
#      else:
#       lines.append(line)
#
# with open('灾害名.txt', 'w', encoding='utf-8') as f:
#     for line in lines:
#      f.write(line)

# def sub_yj():
#     with open(r'代码_文档提交/origin_yj/灾害名.txt', 'r', encoding='utf-8') as f:
#         disaster_name = f.read()
#     result = re.sub(r'(泥石流)' or r'(滑坡)', r'\1}}', disaster_name)
#     print(result)
# if __name__ == '__main__':
#     sub_yj()


# with open(r'代码_文档提交/origin/地点.txt','r',encoding='utf-8') as f:
#     text = f.read()
# result = re.sub(r'(县)', r'\1}}', text)


# def list_add_str(l):
#     return map(lambda x: '{{place:' + x + '}}', l)
#
# list_add_str('广东省惠州市惠东县中澳农牧产业园项目地质灾害危险性评估报告')





# import json
# import re
# import pandas as pd
# import nltk
# # import save_csv
#
# # bltk命令实体案例  提取文本中的人名，地名，机构等等
#
# def parse_document(document):
#     document = re.sub('\n', ' ', document)
#     if isinstance(document, str):
#         document = document
#     else:
#         raise ValueError('Document is not string!')
#     document = document.strip()
#     sentences = nltk.sent_tokenize(document)
#     sentences = [sentence.strip() for sentence in sentences]
#     return sentences
#
#
# # sample document
# text = open(r'test.txt', "r", encoding='utf-8').read()
#
# text1 = ""
# for item in json.loads(text):
#     text1 += " " + item["text"]
# # print(text1)
# # text = """
# # FIFA was founded in 1904 to oversee international competition among the national associations of Belgium,
# # Denmark, France, Germany, the Netherlands, Spain, Sweden, and Switzerland. Headquartered in Zürich, its
# # membership now comprises 211 national associations. Member countries must each also be members of one of
# # the six regional confederations into which the world is divided: Africa, Asia, Europe, North & Central America
# # and the Caribbean, Oceania, and South America.
# # """
#
# # tokenize sentences
# sentences = parse_document(text1)
# tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
# # tag sentences and use nltk's Named Entity Chunker
# tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
# ne_chunked_sents = [nltk.ne_chunk(tagged) for tagged in tagged_sentences]
#
#
#
# # extract all named entities
# named_entities = []
# for ne_tagged_sentence in ne_chunked_sents:
#     for tagged_tree in ne_tagged_sentence:
#         # extract only chunks having NE labels
#         if hasattr(tagged_tree, 'label'):
#             entity_name = ' '.join(c[0] for c in tagged_tree.leaves())  # get NE name
#             entity_type = tagged_tree.label()  # get NE category
#             named_entities.append((entity_name, entity_type))
#             # get unique named entities
#             named_entities = list(set(named_entities))
#
#
# # 存入excel之前
# print(named_entities)
# # store named entities in a data frame
# entity_frame = pd.DataFrame(named_entities, columns=['Entity Name', 'Entity Type'])
# # 存入csv中
# entity_frame.to_csv('data_df.csv', encoding='utf_8_sig')
# # display results
# print(entity_frame)
# # save_csv.save_csv_data(entity_frame)