# Functions go here
def choice_checker (question):

    valid = False
    while not valid:

        # Ask user for choice (and put in lowercase)
        response = input(question).lower()

        # Iterates through list and if response us an item
        # In the list (or the first letter of an item), the
        # Full item name is returned
        for item in valid_list:
            if response == "r" or response == "rock":
            return item

# Main routine goes here

# Ask user for choice and check it's valid
user_choice = choice_checker("Choose rock / paper / scissors (r/p/s): ")

# Print out choice for comparison purposes