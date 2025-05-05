#  -Type-        -Category-	     -Kind-      -Mutable-
# integers	    numerics	    Primitive	    No
# floats	    numerics	    Primitive	    No
# boolean	    booleans	    Primitive	    No
# strings	    text sequences	Primitive	    No
# ranges	    sequences	    Non-primitive	No
# tuples	    sequences	    Non-primitive	No
# lists		    sequences	    Non-primitive	Yes
# dictionaries	mappings	    Non-primitive	Yes
# sets		    sets	        Non-primitive	Yes
# frozen sets   sets	        Non-primitive	No
# functions	    functions	    Non-primitive	Yes
# NoneType	    nulls	        --?--	        No
name = 'you'
def func():
    'This is a function, without an ouput!'

print(type(6))
print(type(6.0))
print(type(True))
print(type(f"Hey {name}!"))
print(type(range(0,5)))
print(type((1, 'pi', True)))
print(type([1, 'pi', True]))
print(type({'key':'value', 'key2':'value2'}))
print(type({1,2,'Georgio',6.0}))
print(type(frozenset({1, 'pi', True})))
print(type(func))
print(type(None))