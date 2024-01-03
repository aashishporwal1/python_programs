rows = 5

for i in range(rows, 0, -1):
    # Add spaces based on the row number
    spaces = " " * (rows - i)
    # Add asterisks
    stars = "* " * i
    # Print the row
    print(spaces+stars)
