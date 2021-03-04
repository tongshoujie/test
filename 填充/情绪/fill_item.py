import re
#regex = re.compile('\[person1\]|\[person2\]|\[person3\]|\[person4\]|\[person5\]')

context=[]
#read the context file
with open("switched_context.txt","r") as con:
    for line in con.readlines():
        line = line.strip('\n')
        context.append(line)
'''
#build keywords array
keywords=['[person1]','[person2]','[person3]','[person4]','[person5]',
          '[job1]',
          '[place1]',
          '[number1]',
          '[country1]',
          '[emotion1]',
          '[ball1]',
          '[building1]',
          '[weather1]',
          '[job1]',
          '[incident1]',
          '[furniture1]',
          '[time1]']
'''
res=[]
################################################################
#build emotion-n
emotion_n=[]
with open("wordlist/emotion-n.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        emotion_n.append(line)

#handle emtion-n
for con in context:
    for key in emotion_n:
        if '[n]' in con:
            newCon = con.replace('[n]',key)
            #print(newCon)
            res.append(newCon)

################################################################
# build emotion-adj
emotion_adj = []
with open("wordlist/emotion-adj.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        emotion_adj.append(line)

# handle emtion-adj
for con in context:
    for key in emotion_adj:
        if '[adj]' in con:
            newCon = con.replace('[adj]', key)
            # print(newCon)
            res.append(newCon)

# merge
set_res = set(res)
for con in context:
    if '[adj]' not in con and '[n]' not in con:
        set_res.add(con)
res = list(set_res)

##############################################################3
#write data into the file
with open("data.txt","w") as f:
    for item in res:
        f.write(item+"\n")
