people = 30
cars = 40
buses = 15

if cars > people:
	print("we should take the cars.")
elif cars < people:
	print("we should not take the cars")
else:
	print("dont know what to do")

if buses > cars:
	print("too many buses")
elif buses < cars:
	print("maybe we can take the buses")
else:
	print("still cannot decide")

if people > buses:
	print("alright, lets take the buses")
else:
	print("lets stay home")
