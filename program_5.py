# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
    # Ask for the budget
    budget = float(input("Enter your budget: "))

    while spent != 0.0:
        spent = float(input("Enter your expense (0 to quit): "))
        total += spent

    # Calculate the difference
    difference = budget - total

    print("Your budget is: $", format(budget, ".2f"))
    print("Spent: $", format(total, ".2f"))

    if difference > 0.0:
        print("You are under budget by $", format(difference, ".2f"))
    elif difference < 0.0:
        print("You are over budget by $", format(difference, ".2f"))
    else:
        print("You are on budget.")


    ######################


if __name__ == '__main__':
    main()