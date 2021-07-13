# declare default languages list
top_languages = ['C', 'C++', 'C#', 'Python', 'JavaScript', 'Java', 'Visual Basic', 'PHP', 'SQL', 'Assembly language']

print(top_languages)

# prompt user for input then compare it to default languages
favorite_language = input("Enter your favorite programming language:  ")

for x in top_languages:
    if x == favorite_language:
        print(favorite_language)
        break