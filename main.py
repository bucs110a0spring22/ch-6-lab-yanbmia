import turtle
wn = turtle.Screen()
fred = turtle.Turtle()
bert = turtle.Turtle()

#part a
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        #print(n)
        count = count + 1
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
    #print(n)                  # the last print is 1
    return(count)

print(seq3np1(3))

num = int(input("Enter # for upper bound range:"))
def main(num):
  start = 0
  if num < 0:
    print("This function works with positive #s only")
    quit()
  for i in range(num):
    start = 1 + start
    print("# of Interations", start, ":", seq3np1(start))
  print("Interations Value (start):", start)
  return(start)

main(num)

#part b
turtle.setworldcoordinates(0,0,10,10)

def setupWindow():
  max_so_far = 0
  for i in range(main(num)):
    result = seq3np1(i)
    if result > max_so_far:
      max_so_far = result
    
  

setupWindow()



