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

################################################################
#build emotion array
emotion=[]
with open("wordlist/character.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        emotion.append(line)
       



################################################################
#handle result
res=[]
#handle emtion
for con in context:
    for key in emotion:
        if '[adj]' in con:
            newCon = con.replace('[adj]',key)
            #print(newCon)
            res.append(newCon)

# merge
set_res = set(res)
for con in context:
    if '[adj]' not in con:
        set_res.add(con)
res = list(set_res)

##############################################################3
#write data into the file
with open("data.txt","w") as f:
    for item in res:
        f.write(item+"\n")
