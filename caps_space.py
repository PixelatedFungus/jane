import pyperclip
def caps_space():
    phrase = input("Enter phrase: ")
    first_item = phrase[0]
    if first_item.isalpha() and first_item.islower():
        new_text = first_item.upper()
    else:
        new_text = first_item
    cut_phrase = phrase[1:]
    for item in cut_phrase:
        if item.isalpha():
            if item.islower():
                new_text = new_text + f" {item.upper()}"
            else:
                new_text = new_text + f" {item}"
        elif item == " ":
            new_text = new_text + "  "
        else:
            new_text = new_text + f" {item}"
    pyperclip.copy(new_text)

caps_space()