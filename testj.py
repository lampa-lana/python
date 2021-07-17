import json

nums = [4, 76, 2, 67, 23, 7, 78, 98]

filename = 'nums.json'
with open(filename, 'w') as f:
    json.dump(nums, f)

file = 'nums.json'
with open(file) as fl:
    nums_new = json.load(fl)

print(nums_new)
