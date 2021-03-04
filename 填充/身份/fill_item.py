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
#build job array
job=[]
with open("wordlist/identity-job.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        job.append(line)
       
#build number array
number = []
with open ("wordlist/identity-number.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        number.append(line)
#build country
country = []
with open ("wordlist/identity-country.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        country.append(line)

place = []
with open ("wordlist/identity-place.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        place.append(line)


################################################################
#handle result
res=[]
#handle country
for con in context:
    for key in country:
        if '[country1]' in con:
            newCon = con.replace('[country1]',key)
            #print(newCon)
            res.append(newCon)

#handle job
for con in context:
    for key in job:
        if '[job1]' in con:
            newCon = con.replace('[job1]',key)
            #print(newCon)
            res.append(newCon)
#handle number
for con in context:
    for key in number:
        if '[number1]' in con:
            newCon = con.replace('[number1]',key)
            #print(newCon)
            res.append(newCon)

#handle place
for con in context:
    for key in place:
        if '[place1]' in con:
            newCon = con.replace('[place1]',key)
            #print(newCon)
            res.append(newCon)


# merge
set_res = set(res)
for con in context:
    if '[job1]' not in con and '[place1]' not in con:
        set_res.add(con)
res = list(set_res)

##############################################################3
#write data into the file
with open("data.txt","w") as f:
    for item in res:
        f.write(item+"\n")
