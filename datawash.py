import jieba
import json
txt = open(r"D:\PyCharm Community Edition 2020.2.2\程序\《在一起》词云\together.txt",'r',encoding='utf-8').read()
word_dict =r"D:\PyCharm Community Edition 2020.2.2\程序\11.txt"
jieba.load_userdict(word_dict)
words = jieba.cut(txt)
# 键值对形式   {}
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word] = counts.get(word,0) +1 #遍历所有，并加1
items = list(counts.items())#键值对变成列表
items.sort(key=lambda x: x[1], reverse=True)
list1=[]
for i in range(200):
    dict1={}
    word, count = items[i]
    dict1['name']=word
    dict1['value']=count
    list1.append(dict1)
print(list1)

with open('tongji.json', 'w', encoding='utf-8') as f:
     f.write(json.dumps(list1,indent=2,ensure_ascii=False))