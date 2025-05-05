def local_greet(locale):
    lang = lang_code(locale)
    region = region_code(locale)
        
    match (lang, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('en', 'AU'):
            return 'Howdy!'
        case ('en', 'CA'):
            return 'Hi!'
        case _:
            return greet(lang)
    
def lang_code(locale):
    return locale[:2]

def region_code(locale):
    return locale.split('.')[0].split('_')[1]

def greet(iso_code):
    match iso_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Hej!'
        case 'af':
            return 'Haai'

print(local_greet('en_US.UTF-8'))
print(local_greet('en_GB.UTF-8'))
print(local_greet('en_AU.UTF-8'))
print(local_greet('en_CA.UTF-8'))
print(local_greet('fr_FR.UTF-8'))
print(local_greet('fr_CA.UTF-8'))
print(local_greet('fr_MA.UTF-8'))
print(local_greet('en_GI.UTF-8'))