# Greeting.
print("Hello!")
print("This is easy madlibs created by me.")
print("As you can see, there are given 3 words in parentheses with quotes below.")
print("You have to put them in sentences, for them to make sense.")
print("Be careful because if you make mistake even in only one letter, your answer will be incorrect.")
print("Words:")

# Making list of words, that challanger should put in their place.

list = ("persue", "happy", "limited")

print(list)

# Writing quotes with one word missing.

print("Quotes:")
print("The most important thing is to enjoy your life - to be _____(1) - it's all that matters.")
print("Your time is _____(2), don't waste it living someone else's life.")
print("In order to be truly happy, you must _____(3) your dreams and goals.")
word1 = input("Word 1: ")
word2 = input("Word 2: ")
word3 = input("Word 3: ")

# qm = quote madlibs. f, s, t stand for "first", "second", "third".

fqm = f"The most important thing is to enjoy your life - to be {word1} - it's all that matters."

sqm = f"Your time is {word2}, don't waste it living someone else's life."

tqm = f"In order to be truly happy, you must {word3} your dreams and goals."

# Writing code that shows is answer correct or not and displays Score below.

c = ("Correct! :)")
i = ("Incorrect! :(")
score = 0
max_score = 3

print(fqm)
if word1 == "happy":
    print(c)
    score += 1
else:
    print(i)

print(sqm)
if word2 == "limited":
    print(c)
    score += 1
else:
    print(i)

print(tqm)
if word3 == "persue":
    print(c)
    score += 1
else:
    print(i)

print("Your score is:", score, "/", max_score)

if score >= 2:
    print("You make it to the next level! :)")
else:
    print("You didn't make it to the next level! :( Try again!")