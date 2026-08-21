# Asks user to enter a number
number = int(input("Enter a number: "))

# Print the times-table from 1 to 10
for i in range(1, 11):
    result = number * i

    # Display the multiplication result
    print(f"{number} x {i} = {result}")