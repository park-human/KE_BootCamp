# Chapter 4 - mission
# 4.1
import random
secret = random.randint(1,10)
guess = random.randint(1,10)

print("secret =",secret)
print("guess =",guess)

if guess > secret:
    print("too low")
elif guess < secret:
    print("too high")
else:
    print("just right")

# 4.2