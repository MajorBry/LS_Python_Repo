def all_caps(text):
    if len(text) > 10:
        return text.upper()
    else:
        return text

print(all_caps('hello world'))
print(all_caps('goodbye'))