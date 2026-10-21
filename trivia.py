
score = 0

print("Basketball Trivia Game")
print("----------------------")

print("\n1. How many players are on the court for one team?")
print("A. 4")
print("B. 5")
print("C. 6")

ans = input("Answer: ").upper()

if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n2. How many points is a free throw worth?")
print("A. 1")
print("B. 2")
print("C. 3")

ans = input("Answer: ").upper()

if ans == "A":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n3. Which team did Michael Jordan win championships with?")
print("A. Lakers")
print("B. Celtics")
print("C. Bulls")

ans = input("Answer: ").upper()

if ans == "C":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n4. How long is an NBA quarter?")
print("A. 10 minutes")
print("B. 12 minutes")
print("C. 15 minutes")

ans = input("Answer: ").upper()

if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\n5. How many points is a shot behind the three-point line worth?")
print("A. 2")
print("B. 3")
print("C. 4")

ans = input("Answer: ").upper()

if ans == "B":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nFinal Score:", score, "/ 5")
