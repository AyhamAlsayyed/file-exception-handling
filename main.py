import random


def generate_numbers(count, max_number, file_name="numbers.txt"):
    """generates random numbers then writes them into file"""
    with open(file_name, "w") as f:
        for i in range(count):
            f.write(f"{random.randint(0, max_number)}\n")


def read_numbers(file_name="numbers.txt"):
    """reads numbers from file"""
    numbers = []
    try:
        with open(file_name) as f:
            for line in f:
                try:
                    numbers.append(int(line))
                except ValueError:
                    pass
            return numbers
    except FileNotFoundError:
        print("File not found")


def calculate(numbers):
    """calculation to list of numbers"""
    if len(numbers) == 0:
        return 0, 0
    total = sum(numbers)
    avg = total / len(numbers)
    return total, avg


def write_result(total, avg):
    """writes results to file"""
    with open("result.txt", "w") as r:
        if total is None:
            r.write("No numbers")
        else:
            r.write(f"The total is: {total}, and the average is: {avg}")


# Main program
count = int(input("how many numbers do you want? "))
max_num = int(input("what do you want the range to be from 0 to : "))

generate_numbers(count, max_num)
write_result(*calculate(read_numbers()))
