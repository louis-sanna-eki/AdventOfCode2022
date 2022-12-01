file = open("./input.txt", "r")
raw = file.read()
file.close()

raw_inventories = list(
    map(lambda raw_inventory: raw_inventory.split("\n"), raw.split("\n\n"))
)
inventories = [list(map(int, raw_inventory)) for raw_inventory in raw_inventories]

sums = list(map(sum, inventories))
result = max(sums)

print("result 1:", result)
