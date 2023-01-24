# Python V 3.9.0

guess_me = 5
number = range(10)

for n in number:
    if n < guess_me:
        print("too low")
    elif n == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
