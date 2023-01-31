# Python V 3.9.0

if __name__ == "__main__":

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
                print(odds[2])

    print(good())
    get_odds()
