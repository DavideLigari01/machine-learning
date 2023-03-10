import random
secret = random.randint(1, 100)
print(secret)
guess = secret+1
for i in range(5):
    guess = int(input("insert a number "))
    if secret == int(guess):
        print("you have won!!!!!!!")
        break
    elif secret < guess:
        print("too large")
    else:
        print("too small")
if guess != secret:
    print("You lost")


def factorial(n):
    result = 1
    for i in range(n):
        result *= i
    return result
