# why write tests?
# reduce bugs in existing code
# ensure bugs that are fixed stay fixed
# ensure that new features or refactoring code doesn't break old ones


#TDD test driven development 
# test first, code sencond 

# red write code that fails
# green minial test code to make test pass
# refactor while test still passes 

# assertions
# make simple assertion with `assert` keyword
# assert accepts an expression 
# returns `None` if the expression is truthy
# raises an `AssertionError` if the expression is falsy
# accepts an optional error message as a second argument

# exampe
def eat_junk(food):
    assert food in ["pizza", "cup cake", "candy"], "food must be chucky with it"
    return f"I love {food} that am grubbing"
food = input("Enter a food please: ")
print(eat_junk(food))

# TO BE CONTINUE...