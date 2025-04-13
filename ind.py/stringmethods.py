sentence="iam A Person Who Loves PHotography"
sentence=sentence.lower()
vowels="aeiou"
consonants="BCDFGHJKLMNPQRSTVWXYZ"
consonants=consonants.lower()
vowel_count=0
consonant_count=0
for i in sentence:
    if i in vowels:
        print("the vowels in sentence are:",i)
        vowel_count+=1
        print("the no of vowels are:,{vowel_count})
for k in sentence:
    if k in consonants:
        print("the consonants in sentence are:",k)
        consonant_count+=1
        print("the no of consonants are:",{consonant_count})
else:
    print("not found:")
