class GoodCat:
    @classmethod
    def what_am_i(cls):
        print("I'm a GoodCat class!")

GoodCat.what_am_i()

class Foo:
    @classmethod
    def bar(cls):
        print('this is bar')

    @classmethod
    def qux(cls):
        print('this is qux')
        cls.bar()

Foo.qux()