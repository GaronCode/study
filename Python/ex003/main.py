def count_str_letters_in_another_str(str1, str2):
    letters = {}
    for str2_letter in str2:
        for str1_letter in str1:
            if str2_letter == str1_letter:
                if not(str1_letter in letters):
                    letters[str1_letter] = 1
                else:
                    letters[str1_letter] += 1
    return letters