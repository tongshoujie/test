import re
context=set()
keys = ['[person1]','[person2]','[person3]','[person4]']
replace_words = ['[person1]','[person2]','[person3]','[person4]']
with open("context.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        context.add(line)
print(context)

switch_context=[]
res=set()
for con in context:
    for key in keys:
        if key in con:
            for rw in replace_words:
                #context.add(con.replace(key,rw))
                res.add(con.replace(key,rw))


# delete: [person1] and [person1] are classmates
list_res = list(res)
temp_list = []
for t in list_res:
    for key in keys:
        cnt = t.count(key)
        if cnt >= 2:
            temp_list.append(t)
for t in temp_list:
    list_res.remove(t)
res = set(list_res)

# merge
for con in context:
    res.add(con)

with open("switched_context.txt","w") as f:
    for re in res:
        f.write(re+"\n")
    """
    for con in context:
        f.write(con+'\n')
    """
    
    
