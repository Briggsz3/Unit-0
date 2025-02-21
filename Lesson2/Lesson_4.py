favorite_languages = {
    'jen': 'python'
    'sarah': 'c'
    'edward': ' rust'
    'phil': 'python'
}

# loop through the key valeus in a dictionary
# the variable can be anything
for name in favorite_languages.keys():
    print(name.title())
print('values'.center('#'))
for name in favorite_languages: # .keys is default behavior so it isn't needed
    print(name.title())

print(*favorite_languages) # prints on same line but you can't do .title()

# looping through keys and values
for name,language in favorite_languages.items():
    print(f"{name}'s favorite programming language is {language}")

