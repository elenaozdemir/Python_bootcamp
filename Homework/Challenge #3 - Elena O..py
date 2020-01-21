# challenge #3:
def extract_digits():
    enter_sentence = str(input("Please enter your sentence: "))
    list = []
    if len(enter_sentence) == 0:
        return None
    for char in enter_sentence:
        if char.isdigit():
            list += char
    return list

print(extract_digits())