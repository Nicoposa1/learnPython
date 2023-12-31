import collections
import time
import re
import sys
print(sys.path)

text = "Hola, tengo 22, mi num es 220932243, hoy es 30"
result = re.findall(r"[0-9]+", text)
print(result)


timestamp = time.time()
local = time.localtime()
resultTime = time.asctime(local)
print(timestamp)
print(resultTime)

numbers = [1, 1, 3, 4, 1, 1]
counter = collections.Counter(numbers)
print(counter)
