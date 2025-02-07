import re

items = re.findall("mul\(\d*,\d*\)", open("data.txt").read())
nums = [re.findall("\d+", i) for i in items]
print(sum(map(lambda x: int(x[0]) * int(x[1]), nums)))
