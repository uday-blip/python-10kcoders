#program to print the map and filter function for numbers divisible by 5
numbers=[2,5,10,55,46,70,28]
div_by5=map(lambda f:f%5==0,numbers)
fil_by5=filter(lambda v:v%5==0,numbers)
print(list(div_by5))
print(list(fil_by5))

#program to print map and filter function for words which have vowels
words=['UDAY','VINAY','BRYN','TYMN','NANI']
vowels=['a','e','i','o','u']
upper_vowels=[]
for i in vowels:
    upper_vowels.append(i.upper())
vowels_are=map(lambda a:any(char in upper_vowels for char in a),words)
filtered_vowels=filter(lambda b:any(char in upper_vowels for char in b),words)
print(list(vowels_are))
print(list(filtered_vowels))

    
