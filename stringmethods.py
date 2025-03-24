sentence="iam A Person Who Loves PHotography"
sentence=sentence.lower()
vowels="aeiou"
consonants="BCDFGHJKLMNPQRSTVWXYZ"
consonants=consonants.lower()
for i in sentence:
    if i in vowels:
        print("the vowels in sentence are:",i)
for k in sentence:
    if k in consonants:
        print("the consonants in sentence are:",k)
else:
    print("not found:")