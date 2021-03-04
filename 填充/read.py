# 文件读取方式
import json
f = open("json_data.json", mode = 'r', encoding = 'utf-8')
dicts = json.load(f)
f.close()   # 注意 dicts[0]是文件信息，所以从dicts[1]开始才是真正的context字典