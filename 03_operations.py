set_a = {"COL", "MEX", "BOL"}
set_b = {"COL", "BRA", "PER"}

# Union
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# Intersection
set_d = set_a.intersection(set_b)
print(set_d)
print(set_a & set_b)

# Difference
set_e = set_a.difference(set_b)
print(set_e)
print(set_a - set_b)

# Symmetric difference
set_f = set_a.symmetric_difference(set_b)
print(set_f)
print(set_a ^ set_b)
