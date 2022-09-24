import random
name = input("Enter your name: ")
print(f'Hello {name}! welcome to the Word Guessing Game')
words = ["Pyhton", "java", "instagram", "facebook", "Telegram", "college"]
index = random.randint(0, len(words))
word = words[index]
indexes = random.sample(range(0, len(word)), 3)
guesses = "" 
for i in indexes:
    guesses += word[i]

chances = 10
while chances>0:
    won = True
    for ch in word:
        if ch in guesses:
            print(ch, end = '')
        else:
            print("_" , end = '')
            won = False
    if won:
        print("/n You won!")
        print(f"Your score is {chances*10}")
        break
              
    guess = input("/n Guess a charachter: ")
    guesses += guess
    
    if guess not in word:
        chances -=1
        print("/n wrong answer")
        print(f"You have {chances}")
    if chances == 0:
        print("you lose")
        break
            
    