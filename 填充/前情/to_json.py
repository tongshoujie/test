import re
import json

persons = ['[person1]', '[person2]', '[person3]', '[person4]']

# 设置全局列表
dict_list = []

# 读数据
data = []
with open("data.txt", "r") as d:
    for line in d.readlines():
        line = line.strip("\n")
        data.append(line)
# 设置模板 id 字典， 用于后面计算每个context的template_id
template_dict = {}
tem_id = 0
with open("context.txt", "r") as con:
    for line in con.readlines():
        line = line.strip("\n")
        template_dict[line] = tem_id
        tem_id += 1
# 本文件基本信息
remember_list = {"type": "antecedent"}
remember_list.update(template_dict)
dict_list.append(remember_list)

# main
context_id = 0
for d in data:
    context = d
    max_person = 0
    template_id = 0
    d_list = list(d.split(' '))
    for p in persons:
        if p in d:
            max_person = max(max_person, int(p[-2]))

    for k, v in template_dict.items():
        k_list = list(k.split(' '))
        if len(k_list) != len(d_list):
            continue
        similarity = 0
        cnt = 0  # count [xxxx]
        for i, j in zip(k_list, d_list):
            if i[0] == '[':
                cnt += 1
                continue
            if i == j:
                similarity += 1
        if similarity == len(k_list) - cnt:
            template_id = v
            break

    dic = {
        "context_id": context_id,
        "context": context,
        "type": "antecedent",
        "template_id": template_id,
        "max_person": max_person
    }
    dict_list.append(dic)
    context_id += 1
# 写入
with open('json_data.json', mode='w', encoding='utf-8') as f:
    json.dump(dict_list, f, indent=4)