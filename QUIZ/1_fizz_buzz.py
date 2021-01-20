for i in range(1,101):
    test_string = ""
    if i%3 == 0: test_string+="Fizz"
    if i%5 == 0: test_string+="Buzz"
    print test_string or i
