def print_upper_words(words, must_start_with):
    """filters out words that dont start with the letters provided
    and prints them in all caps
    """

    new_words = []

    for word in words:
        new_words.append(word.lower())
    
    for word in new_words:
        if word[0] in must_start_with:
            print(word.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"h", "y"})
