# Python V 3.9.0

if __name__ == "__main__":
    things = ["mozzarella", "cinderella", "salmonella"]
    print(things)

    print(things[1].capitalize())

    print(things)

    # 7.5 No, the element did not change

    things[0] = things[0].upper()

    print(things)

    del things[2]

    print(things)
