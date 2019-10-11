#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) as the only iteration it has is itself


b) O(n ^2) as it has two iterations, for loop -> while loop


c) This is recursive and I believe its O(2 +n!)

## Exercise II

Task: Determine the value of F so that the number of dropped + broken eggs is minimized

We need to keep track of the following
current_floor
dropped_eggs
has_broken = false (or true)

then we can use a for loop to go over all of the floors in the array
while has_broken = false
	drop the egg
	if the egg didnt break we increment dropped_eggs + 1
	current_floor + 1
	continue
else:
	if the egg broke we increment the number of eggs dropped
	has_broken = true
	current_floor + 1
	continue

Runtime complexity = O(n^2) as it has two iterations for loop -> while loop


