def write_and_read_file():
    filename = "output.txt"

    # Step 1: Take user input and write it to the file
    user_input = input("Enter some text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
        print('The data is succesfully written in output.txt')


    # Step 2: Append additional data
    more_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(more_input + '\n')
        print('The data is succesfully append  in output.txt')

    # Step 3: Read and display the final content of the file
    print(f"\nFinal contents of '{filename}':\n")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())


# Run the function
write_and_read_file()
