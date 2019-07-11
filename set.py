blue_eyes = {'olivia','harry','lily','jack','amilia'}
blonde_hair = {'harry','jack','amilia','mia','joshua'}
smell_hcn = {"harry","amilia"}
test_ptc = {'harry','lily','amilia','lola'}
o_blood = {'mia','joshua','lily','olivia'}
b_blood = {'amilia','jack'}
a_blood = {'harry'}
ab_blood = {'joshua','lola'}

print(blue_eyes.union(blonde_hair))

print(blonde_hair.intersection(blue_eyes))

print(blonde_hair.difference(blue_eyes))

print(blonde_hair.symmetric_difference(blue_eyes))

print(smell_hcn.issubset(blonde_hair))

print(test_ptc.issuperset(smell_hcn))

print(a_blood.isdisjoint(o_blood))
