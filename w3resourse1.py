#  Write a Python program to convert JSON data to Python object.
import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\npython data:")
print(python_obj)


