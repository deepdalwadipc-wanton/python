# basic string methods
#strings are immutable
sentence = "dont view this file mf  123       "
sentence2 = "just kidding"
#string slicing
print(sentence[0:10])   #postive slicing
print(sentence[-10:-1]) #negatie slicing    
print(sentence[:0:-1])  #backward slicing
print(sentence[::1])    #forward slilcing

#string methods
newsentence1 = sentence.lower()
print(newsentence1)
newsentence2 = sentence.upper()
print(newsentence2)

print(sentence.strip(),sentence2)

print(sentence.replace("view","see"))

print(sentence.count("i"))

print(sentence.startswith("dont"))
print(sentence2.endswith("ing"))

print(sentence.isalpha())   #checks if the string is only words

print(sentence.isdigit())   #checks if the string is only digit

print(sentence.title())

