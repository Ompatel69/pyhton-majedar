#aaj doc strings sikhnege yeh comment hai woh ignore karta hai python interpreter but docstring ko special treatment milta hai
def square(n):
    '''take input of n,and returns the square of n'''
    print(n**2)
square(2)
print(square.__doc__)#yeh samja doc string line ko print kiya and only def ke niche wale line meh hi doc likega toh aayega
#done

