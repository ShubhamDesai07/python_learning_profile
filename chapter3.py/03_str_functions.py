name = "anishop"

print(len(name))
print(name.endswith("op")) # gives True
print(name.endswith("opz")) # give False
print(name.startswith("ani")) # give true
print(name.startswith("Ani")) # give false
print(name.capitalize()) # capitals the first letter from anishop to Anishop
count = name.count("a")# counts and print number of "c"
print(count)
find = name.find("op")# finds the word and give you index value
print(find)
replace = name.replace("op","OP")# replaces the word
print(replace)
print(name.title())
print(name.upper())