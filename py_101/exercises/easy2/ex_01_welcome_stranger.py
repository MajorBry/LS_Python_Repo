def greetings(name, job):
    return f'Hello, {' '.join(name)}! Nice to have a {job['title']} {job['occupation']} around.'

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
