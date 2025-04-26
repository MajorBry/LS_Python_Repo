# ↓Assumes that language code is the first two characters in the locale code.
def lang_code(locale):
    return locale[:2]

print(lang_code('en_US.UTF-8'))
print(lang_code('en_GB.UTF-8'))
print(lang_code('ko_KR.UTF-16'))
