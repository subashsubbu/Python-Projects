import random

# user = input('Guess the secret number:  ')
# computer = random.choice([1,100])

# if user == computer:
#     print('You guessed right! You won!!!')
    
# if user != computer:
#     print('You lose! Try again!!!')
    
    
def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess any number from 1 to {x}: '))
        if guess > random_number:
            print('Too High')
        elif guess < random_number:
            print('Too low')
    
    print(f'You have guessed the number {random_number} correctly')
    
    
guess(10)
    
