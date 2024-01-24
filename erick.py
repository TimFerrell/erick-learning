def main():
    # The print function writes text to stdout (which is
    # typically text output to the terminal)
    print("Hey! What's your name?")

    # On this line, we'll add the end parameter
    # so that the cursor doesn't go to the next line
    # and puts the prompt on the same line as "Name:"
    print("Name: ", end=" ")

    # "input" is what's called a blocking function,
    # and it waits on the user to hit Enter before
    # allowing the program to continue executing
    name = input()

    # Here we get the result from the input function
    # which is returned as a string, and combine a
    # few strings together to form a single string.
    # Plus symbols are used to combine multiple strings
    # together. The print function only accepts a single
    # string, so we must combine them.
    print("Hello " + name + "! Nice to meet you.")

# While the main function is defined above, we must invoke
# the function here to actually execute it
main()
