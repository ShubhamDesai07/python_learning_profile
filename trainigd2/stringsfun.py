#text =  " hello world"
#print(text)
#print(text.strip())


text =  " hello world"
print(text)
print(text.split())
text1="apple,banana,cherry"
print(text1.split(","))


text2=["apple","banana","cherry"]
print(("--".join(text2)))


text4 =  " hello world"

reversed_str = text4[::-1]
print(reversed_str)

#palinderome

wow = "madam"
reversed = wow[::-1]
if wow == reversed:
    print("palindrome")
else:
    print("not palindrom")    


