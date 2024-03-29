def max(numbers):                       #the max number calculator
    highest_number = 0
    for item in numbers:
        if item >= highest_number:
            highest_number = item
    return highest_number
