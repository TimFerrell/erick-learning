def main():
    # The print function writes text to stdout (which is
    # typically text output to the terminal)
    print("Hey! What's your name?")

    # On this line, we'll add the end parameter
    # so that the cursor doesn't go to the next line
    # and puts the prompt on the same line as "Name:"
    # print("Name: ", end=" ")

    # "input" is what's called a blocking function,
    # and it waits on the user to hit Enter before
    # allowing the program to continue executing
    name = input("Name: ")

    # Here we get the result from the input function
    # which is returned as a string, and combine a
    # few strings together to form a single string.
    # Plus symbols are used to combine multiple strings
    # together. The print function only accepts a single
    # string, so we must combine them.
    print("Hello " + name + "!")

    # This is a super basic if/else block
    # "==" is used to test equality between two things
    if name == "Tim":
        print("I'm getting kind of bored of you. >:(")
    else:
        # If the initial statement isn't met, you can call
        # alternative code in the else block
        print("I'm glad to see you!")

    print("How old are you?")
    # print("Age: ", end="")

    # Because input returns a string, we'll use the
    # int() function to *cast* a string into an integer.
    age = int(input("Age: "))

    print("For each year you've been alive I'll give you a star!")

    # This is a basic "for" loop. range() is used in Python to
    # iterate over a range of numbers. In this loop, the indented
    # code will be called the number of times in the range() function
    for x in range(age):
        print("⭐", end="")

    print("Bye!")


# While the main function is defined above, we must invoke
# the function here to actually execute it
main()


test commit