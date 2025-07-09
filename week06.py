def load_to_list(filepath: str) -> list[float]:
    results = []
    file = open(filepath, "r")
    for line in file:
        value = float(line.strip())
        results.append(value)
    file.close()
    return results

def descriptive_statistics(source_data: list[float]) -> None:
    total = 0
    for value in source_data:
        total = total + 1

    sum_values = 0
    for values in source_data:
        sum_values = sum_values + value

    average = sum_values / total

    smallest = source_data[0]
    for value in source_data:
        if value < smallest:
            smallest = value

    largest = source_data[0]
    for value in source_data:
        if value > largest:
            largest = value 

    print(f"There are {total} values in the data source.")
    print(f"The average value is {round(average, 2)}")
    print(f"The highest value is {largest} and the smallest value is {smallest}.")

def apply_markup(filepath: str) -> None:
    file = open(filepath, "r")
    for line in file:
        words = line.strip().split()
        new_line = ""
        for word in words:
            if word.startswith ("."):
                new_word = word [1:].upper()
            elif word.startswith("_"):
                letters = list(word[1:])
                new_word = " ".join(letters) 
            else:
                new_word = word 
            new_line = new_line + new_word + " "
        print(new_line.strip())
    file.close()


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  DO NOT MODIFY THE CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 

