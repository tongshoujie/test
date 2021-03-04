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
          '[time1]',
          '[relative1]']
'''

################################################################
#build ball array
ball=[]
with open("wordlist/antecedent-ball.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        ball.append(line)
       
#build incident array
incident = []
with open ("wordlist/antecedent-incident.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        incident.append(line)
#build country
country = []
with open ("wordlist/identity-country.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        country.append(line)

# build country
Relative = []
with open("wordlist/Relative.txt", "r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        Relative.append(line)

################################################################
#handle result
res=[]
#handle ball
for con in context:
    for key in ball:
        if '[ball1]' in con:
            newCon = con.replace('[ball1]',key)
            #print(newCon)
            res.append(newCon)

#handle incident
for con in context:
    for key in incident:
        if '[incident1]' in con:
            newCon = con.replace('[incident1]',key)
            #print(newCon)
            res.append(newCon)
#handle conutry
for con in context:
    for key in country:
        if '[country1]' in con:
            newCon = con.replace('[country1]',key)
            #print(newCon)
            res.append(newCon)

# handle relative
for con in context:
    for key in Relative:
        if '[relative1]' in con:
            newCon = con.replace('[relative1]', key)
            # print(newCon)
            res.append(newCon)

# merge
set_res = set(res)
for con in context:
    if '[incident1]' not in con and '[relative1]' not in con:

        set_res.add(con)
res = list(set_res)

#write data into the file
with open("data.txt","w") as f:
    for item in res:
        f.write(item+"\n")
