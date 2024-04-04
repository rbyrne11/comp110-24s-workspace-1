"""Demonstrating dictionary utility functions."""

author: str = "730410363"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Determine if duplicates are present."""
    invert_dict: dict[str, str] = {}
    for key, value in input_dict.items():
        if value in invert_dict:
            raise KeyError("Duplicates cannot be present!")
        invert_dict[value] = key
    return invert_dict 


def favorite_color(inputs: dict[str, str]) -> str:
    """Determine most frequent color."""
    color_amounts: dict[str, int] = {}
    for color in inputs.values():
        if color in color_amounts:
            color_amounts[color] += 1
        else:
            color_amounts[color] = 1
    
    highest_count = 0
    maximum_color = ""
    for color, count in color_amounts.items():
        if count > highest_count:
            highest_count = count
            maximum_color = color
    return maximum_color
        
    
def count(values: list[str]) -> dict[str, int]:
    """Determine amount of appearances of the value within the list."""
    count: dict[str, int] = {}
    for item in values: 
        if item in count: 
            count[item] += 1
        else: 
            count[item] = 1
    return count


def alphabetizer(term: list[str]) -> dict[str, list[str]]:
    """Organize alphabetically."""
    random_words: dict[str, list[str]] = {}
    for word in term:
        letter1 = word[0].lower()
        if letter1 in random_words:
            random_words[letter1].append(word)
        else:
            random_words[letter1] = [word]
    return random_words

    
def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Update attendance log."""
    if day in attendance:
        attendance[day].append(student)
    else:
        attendance[day] = [student]