
def count_down(num_input):  # recursive function
    if num_input == 0:  # base case
        print("Done!")
    else:  # recursive statement
        num_input -= 1
        print("    counting...", num_input)
        count_down(num_input)


num = ' '
while (num == ' '):  # input validation loop
    try:
        num = int(input("Please enter a number to count down to zero from:\n"))

    except:
        print("Please enter a number.")


print("You typed in:  ", num)
count_down(num)
