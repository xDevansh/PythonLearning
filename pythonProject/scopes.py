#SCOPE
"""
LEGB
local, enclosing, global,bultin
"""
x="global x"

def test():
	x='local x'
	print(x)
test()
print(x)

print('==============================')

def outer():
	#x='outer x'
	def inner():
		x='inner x'
		print(x)
	inner()
	print(x)

outer()
print(x) #outside function outer


#use 'global x' in outer() tp use global var, or
print("""==============================
	changing the local var of outer fn in inner fn
	""")
print("""
input:
def outer1():
    x = "outer x"

    def inner1():
        nonlocal x
        x = "modified by inner"
        print("Inside inner:", x)

    print("Before calling inner:", x)
    inner()
    print("After calling inner:", x)

outer()
output:
""")
def outer():
    x = "outer x"

    def inner():
        nonlocal x
        x = "modified by inner"
        print("Inside inner:", x)

    print("Before calling inner:", x)
    inner()
    print("After calling inner:", x)

outer()

