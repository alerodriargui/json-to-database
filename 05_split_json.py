import json
import math

with open("reservations.json") as f:
    data = json.load(f)

chunk_size = math.ceil(len(data) / 10)

for i in range(10):
    with open(f"part_{i}.json", "w") as out:
        json.dump(
            data[i*chunk_size:(i+1)*chunk_size],
            out,
            indent=4
        )
