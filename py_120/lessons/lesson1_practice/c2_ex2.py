class Foo:
    def __init__(self):
        class_name1 = type(self).__name__
        class_name2 = self.__class__.__name__
        print(f'I am a {class_name1} object')
        print(f'I am a {class_name2} object')

bar = Foo()