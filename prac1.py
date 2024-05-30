if __name__ == '__main__':
    try:
        # Read the number of integers
        n = int(input("Enter the number of elements: "))
        
        # Check if n is a positive integer
        if n <= 0:
            raise ValueError("The number of elements must be a positive integer.")

        # Read the integers as a list of strings
        integer_list = list(map(int, input().split()))

        # Validate if the number of integers matches n
        if len(integer_list) != n:
            raise ValueError(f"Expected {n} integers, but got {len(integer_list)}.")

        # Convert the list of strings to a list of integers
        integer_list = list(map(int, integer_list))

        # Convert the list of integers to a tuple
        tup = tuple(integer_list)

        # Print the hash of the tuple
        print(hash(tup))

    except ValueError as e:
        print(f"Invalid input: {e}")