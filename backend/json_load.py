import json

machine_info = {}
with open('machineInfo.json') as json_file:
    machine_info = json.load(json_file)

print(machine_info["0"])
