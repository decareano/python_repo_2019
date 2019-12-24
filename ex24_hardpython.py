print("lets practice")
print('you\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.') 

poem = """
\tThe lovely world
with login so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")


five = 10 - 2 + 3 - 6
print("this should be five: %s" % five)

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates

started = 10000
beans, jars, crates = secret_formula(started)

print("with starting point of: %d "  % started)
print("we would have %d beans, %d jars, and %d crates. " % (beans, jars, crates))

a_test = started / 10

print("we can also do it this way:")
print("We woudl have %d beans, %d jars, %d crates." % secret_formula(a_test))
