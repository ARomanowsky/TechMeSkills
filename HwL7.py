# Exercise 1
print('-----Exercise 1-----')

words = ('pip', 'hello', 'mum', 'tree', 'lol', 'phyton', 'redivider')

def palindrom(word):
    if word == word[::-1]:
        return True

print(f'In the tuple following palindromes: {list(filter(palindrom, words))}')

# Exercise 2
print('-----Exercise 2-----')

sentence = (input("Enter two words throught space: ")).split()

print(f'First method:  !{sentence[1]} ! {sentence[0]}!')

print("Second method: " '!{0} ! {1}!'.format(sentence[1], sentence[0]))

sentence.reverse()
print(f'Third method:  !{" ! ".join(sentence)}!')






