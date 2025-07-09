temperatureFilePath = "data/temperatures.txt"
markupFilePath = "data/markup.txt"

def load_to_list(filepath: str) -> list[float]:
    """
    Read one temperature per line from a text file and return them
    as a list of floats.
    """

    # Store values here
    temperatures = []   

    with open(filepath, "r") as file:
        for line in file:
            if line != "": # Check if a blank line
                temperatures.append(float(line))

    # Return the list of temperatures from the file
    return temperatures


def descriptive_statistics(source_data: list[float]) -> None:
    """
    Print simple descriptive statistics for a list of temperatures.
    """
    # Check to make sure list is not empty
    if len(source_data) == 0:
        print("No data provided.")
    else:
        # Gather statistics
        count = len(source_data)
        avg = round(sum(source_data) / count, 2)
        high = max(source_data)
        low = min(source_data)

        # Print out the statistics.
        print(f"There are {count} values in the data source.")
        print(f"The average value is {avg}")
        print(f"The maximum value is {high} and the minimum value is {low}.")

descriptive_statistics(load_to_list(temperatureFilePath))


def apply_markup(filepath: str) -> None:
    """
    Read a text file line by line and apply two mark-up rules:
    
    - A word that begins with a dot is printed in UPPERCASE
    - A word that begins with an underscore is printed in expanded form, with spaces between every letter.
    """
    # Open the file and process one line at a time.
    with open(filepath, "r") as file:
        for row in file:
            line = row.rstrip("\n") # Read the file every line

            tokens = line.split() # Split into words per line
            processed_tokens = [] # Collect transformed words
    
            for token in tokens:
                if token.startswith("."):
                    processed_tokens.append(token[1:].upper())
                elif token.startswith("_"):
                    processed_tokens.append(" ".join(token[1:]))
                else:
                    processed_tokens.append(token)

            # Put words back together and print the transformed line.
            print(" ".join(processed_tokens))

apply_markup(markupFilePath)


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

