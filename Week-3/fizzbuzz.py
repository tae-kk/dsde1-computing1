for x in range(1,101):
    if x % 3 == 0  and x % 5 != 0:
        print("Fizz")
        continue
    if x % 5 == 0 and x % 3 != 0:
        print("Buzz")
        continue
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
        continue
    print(x)
  
