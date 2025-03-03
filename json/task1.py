import json 

with open("/Users/aliaskarmussin/Desktop/PP2-spring-2025/lab4/json/sample-data.json", "r") as file:

    data = json.load(file)

print("Interface Status")

print("=" * 80)

print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")

print("-" * 80)

for item in data["imdata"]:

    attributes = item["l1PhysIf"]["attributes"]

    dn = attributes["dn"]

    description = attributes["descr"] if attributes["descr"] else ""

    speed = attributes["speed"]

    mtu = attributes["mtu"]

    print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")