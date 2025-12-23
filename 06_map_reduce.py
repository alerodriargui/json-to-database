import json
from datetime import datetime

def map_file(filename):
    result = {}
    with open(filename) as f:
        data = json.load(f)

    for r in data:
        days = (
            datetime.fromisoformat(r["Checkout"]) -
            datetime.fromisoformat(r["Checkin"])
        ).days

        result[r["Room"]] = result.get(r["Room"], 0) + days

    return result


final = {}

for i in range(10):
    partial = map_file(f"part_{i}.json")
    for room, days in partial.items():
        final[room] = final.get(room, 0) + days

with open("occupancy.json", "w") as f:
    json.dump(final, f, indent=4)
