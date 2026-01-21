'''text = "Hello world"
text = text.lower()
vowels = "aeiou"
v_count = 0
c_count = 0


for char in text:
    if char in vowels:
        v_count+=1
    else:
        c_count+=1

print("vowels",v_count)
print("consonents",c_count)'''

text = "hello how are you?"
word ="how"
text = text.lower()
word = word.lower()
if word in text:
    print(f"'{word}' is present in the text.")
else:
    print(f"'{word}' is not present in the text.")


           