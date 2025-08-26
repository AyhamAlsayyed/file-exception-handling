import random

with open("numbers.txt", "w") as f:
    for i in range(10):
        f.write(f"{random.randint(1, 99)}\n")

numbers = []
try:
    with open("numbers.txt") as f:
        for line in f:
            try:
                numbers.append(int(line))
            except ValueError:
                pass
except FileNotFoundError:
    print("File not found")

if len(numbers) == 0:
    print("No numbers found")
else:
    total = sum(numbers)
    with open("result.txt", "w") as r:
        r.write(f"The total is: {total}, and the average is: {total/len(numbers)}")
