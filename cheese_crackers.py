def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("you have %d cheeses!" % cheese_count)
	print("you have %d boxes of crackers" % boxes_of_crackers)
	print("man that's enough of a party")
	print("get a blanket.\n")

print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("or, we can use variables from our script:")
cantidad_cheese = 33320
cantidad_crackers = 50


cheese_and_crackers(cantidad_cheese, cantidad_crackers)

print("we can do even math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("we can combine the two variables and match:")
cheese_and_crackers(cantidad_cheese + 200, cantidad_crackers + 23)
