def first_non_repeating_letter(string):
    string_lower = string.lower()
    for i, letter in enumerate(string_lower):
        if string_lower.count(letter) == 1:
            return string[i]


print(first_non_repeating_letter('ssttrr'))
print(first_non_repeating_letter('stress'))
print(first_non_repeating_letter('sTress'))
