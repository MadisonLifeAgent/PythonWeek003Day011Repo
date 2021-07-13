def language_check():
    # declare default languages list
    top_languages = ['C', 'C++', 'C#', 'Python', 'JavaScript', 'Java', 'Visual Basic', 'PHP', 'SQL', 'Assembly language']

    print(top_languages)

    # prompt user for input then compare it to default languages
    favorite_language = input("Enter your favorite programming language:  ")

    # check to see if user's favorite langugage is in list of languages
    if favorite_language in top_languages:
        print(favorite_language)
    else:
        print("language not found")

language_check()