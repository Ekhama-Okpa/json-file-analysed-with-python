
import json, pprint

# loading the JSON File
with open("daikibo-telemetry-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# setting the parameters
machines = []                       """All the nine machines in a list."""
failedMachines = {}                 """Nested dictionary with number of fails per machine in each location."""
n = 0                               """Loop parameter."""
highestNumber = 0                   """The number of fails with the machine with most number of fails overall."""
mostFailsMachine = ""               """The name of the machine that broke down the most."""
mostFailsLocation = ""              """The location that had the machine that broke down the most."""

# obtaining the names of all the nine different machines and putting them in the "machines" list
for dictionary in data:
    for parameter in dictionary.keys():
        if parameter == "deviceType":
            if dictionary["deviceType"] not in machines:
                machines += [dictionary["deviceType"]]

# counting the total number of fails per machine in every location
for dictionary in data:
    failedMachines.setdefault(data[n]['location']['city'], {machinery: 0 for machinery in machines})
    if dictionary.get("data", {}).get("status", {}) == "unhealthy":
        failedMachines[data[n]['location']['city']][f'{data[n]["deviceType"]}'] += 1
    n += 1
    continue

# obtaining which location and which machine there had the most breakdowns
for dictionary in failedMachines:
    for key in failedMachines[dictionary]:
        if failedMachines[dictionary][key] > highestNumber:
            highestNumber = failedMachines[dictionary][key]
            mostFailsMachine = key
            mostFailsLocation = dictionary

print(f"The {mostFailsMachine} in {mostFailsLocation} had the most fails with {highestNumber} fails.")
