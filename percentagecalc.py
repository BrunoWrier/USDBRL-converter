# Python 3 program to calculate
# the percentage

# Function to calculate the percentage
def percent(a, b):
    result = float(((b - a) * 100) / a)

    return result


# Driver code
if __name__ == "__main__":
    a, b = 20, 25

    # Function calling
    print(percent(a, b), "%")

# This code is contributed by ANKITRAI1
