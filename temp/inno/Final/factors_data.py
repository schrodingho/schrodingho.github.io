import json
with open("f1.json",'rb') as load_f:
    load_dict = json.load(load_f)
    print(load_dict)
