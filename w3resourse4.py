import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print('original dict:',j_str)
print(json.dumps(j_str, sort_keys=True, indent=4))
print('______________________________________________')
import json
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
d={}
for i in sorted(j_str.keys()):
    d[i]=j_str[i]
print(json.dumps(d,indent=4))
print('_______________________________________________')
