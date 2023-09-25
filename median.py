"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        numbers = [
            float(value)
            for value in input("Enter a list of numbers separated by commas: ").split(
                ","
            )
        ]
        numbers.sort()
        if len(numbers) % 2 == 0:
            median_low = numbers[round(len(numbers) / 2) - 1]
            median_high = numbers[round(len(numbers) / 2)]
            median = (median_high + median_low) / 2
        else:
            median = numbers[round(len(numbers) / 2)]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median)
