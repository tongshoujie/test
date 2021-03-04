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
#read the words file and build emotion array
emotion=[]
with open("wordlist/environment-emotion.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        emotion.append(line)
       
#build building array
building = []
with open ("wordlist/environment-building.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        building.append(line)
#build furniture
furniture = []
with open ("wordlist/environment-furniture.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        furniture.append(line)
#build season
season = []
with open ("wordlist/environment-season.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        season.append(line)
#build time
time = []
with open ("wordlist/environment-time.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        time.append(line)
#build weather
weather = []
with open ("wordlist/environment-weather.txt","r") as f:
    for line in f.readlines():
        line = line.strip('\n')
        weather.append(line)

################################################################
#handle result
res=[]
#handle emotion
for con in context:
    for key in emotion:
        if '[emotion1]' in con:
            newCon = con.replace('[emotion1]',key)
            #print(newCon)
            res.append(newCon)

#handle building
for con in context:
    for key in building:
        if '[building1]' in con:
            newCon = con.replace('[building1]',key)
            #print(newCon)
            res.append(newCon)
#handle furniture
for con in context:
    for key in building:
        if '[furniture1]' in con:
            newCon = con.replace('[furniture1]',key)
            #print(newCon)
            res.append(newCon)           
#handle season
for con in context:
    for key in season:
        if '[season1]' in con:
            newCon = con.replace('[season1]',key)
            #print(newCon)
            res.append(newCon)
#handle time
for con in context:
    for key in time:
        if '[time1]' in con:
            newCon = con.replace('[time1]',key)
            #print(newCon)
            res.append(newCon)
#handle weather
for con in context:
    for key in weather:
        if '[weather1]' in con:
            newCon = con.replace('[weather1]',key)
            #print(newCon)
            res.append(newCon)

# merge
set_res = set(res)
for con in context:
    if '[weather1]' not in con and '[emotion1]' not in con:
        set_res.add(con)
res = list(set_res)

##############################################################3
#write data into the file
with open("data.txt","w") as f:
    for item in res:
        f.write(item+"\n")
