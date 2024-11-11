# Armstrong.py

def is_armstrong(num):
    # Convert number to string to easily access each digit
    digits = str(num)
    power = len(digits)  # Number of digits
    sum_of_powers = sum(int(digit) ** power for digit in digits)

    return sum_of_powers == num

def generate_armstrong_numbers(start, end):
    return [num for num in range(start, end+1) if is_armstrong(num)]






# main.py
import Armstrong

# Define the range
start = 1
end = 1000

# Generate Armstrong numbers between the range
armstrong_numbers = Armstrong.generate_armstrong_numbers(start, end)

# Print the Armstrong numbers
print(f"Armstrong numbers between {start} and {end}:")
print(armstrong_numbers)

~                                       




