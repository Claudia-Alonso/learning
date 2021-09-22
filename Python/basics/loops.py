def main():
  x = 0

  # define a while loop
  # while (x<5):
  #   print(x)
  #   x=x+1

  # define a for loop
  # for x in range(5, 10): # x loops over a range of numbers, in this case 5,6,7,8,9. 10 is not included in the range
  #   print(x)

  # use a for loop over a collection
  # days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  # for d in days: 
  #   # in each iteration d will be set to the current item that it's looking at that time through the loop.
  #   print(d)
  
  # use the break and continue statements
  # for x in range (5, 10):
  #   #if (x==7): break # The break statement will cause the for loop to terminate
  #   if (x%2 == 0): continue
  #   # Continue basically means skip the rest of the execution of this loop. 
  #   # So, just go back up to the top of the loop, 
  #   # and start with the next value. So, don't do this statement right here that's in the loop.
  #   print(x)

  #using the enumerate() function to get index 
  # The enumerate function will iterate over this collection like loop normally would, 
  # but in addition to returning the value of the item being looked at, 
  # it also returns a value that is the index of the item in question. 
  # This function is going to return two values. It's going to return the index of the member 
  # of the collection that we're looking at, as well as the actual member of the collection.
  days=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
  for i,d in enumerate(days): 
    print(i, d)
  
if __name__ == "__main__":
  main()
