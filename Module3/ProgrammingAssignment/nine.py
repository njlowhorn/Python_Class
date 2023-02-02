# Python V 3.9.0

def good():
    character_list = ["Harry", "Ron", "Hermione"]
    return character_list

def get_odds():
    odds = []
    for i in range(10):
        if i % 2 != 0:
            odds.append(i)
    print(odds)

    for item in odds:
        if item == odds[2]:
            yield odds[2]

if __name__ == "__main__":

    print(good())
    for i in get_odds():
        print(i)
