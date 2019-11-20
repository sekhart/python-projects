from collections import OrderedDict

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

favorite_languages1 = OrderedDict()

favorite_languages1['jen'] = 'python'
favorite_languages1['sarah'] = 'c'
favorite_languages1['edward'] = 'ruby'
favorite_languages1['phil'] = 'python'

for name, languages in favorite_languages1.items():
    print("\n" + name.title() + "'s favorite languages are:" + languages.title())
