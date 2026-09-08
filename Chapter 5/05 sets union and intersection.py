s1 = {1,2,3,54,65}
s2 = {2,3,54,53,87,98}
# print(s1.union(s2)) # simple mathematical sets operation which we
# print(s1.intersection(s2))# have studied in cass 11 and 12th
# print(s1.difference(s2))# s1 - s2
# print(s2.difference(s1))# s2 - s1
print(s1.symmetric_difference(s2))# elements which are in s1 or s2 but not in both
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))
print(s1.discard(54))
