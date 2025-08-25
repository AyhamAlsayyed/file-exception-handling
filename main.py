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
    total = 0
    for number in numbers:
        total += number
    with open("result.txt", "w") as r:
        r.write(f"The total is: {total}, and the average is: {total/len(numbers)}")
