import json

with open('ghi.txt') as f:
  state_data= json.load(f)

for state in state_data['states']:
  del state['ghi.txt']

with open('new_states.json', 'w') as f:
  json.dump(state_data, f, indent=2)
