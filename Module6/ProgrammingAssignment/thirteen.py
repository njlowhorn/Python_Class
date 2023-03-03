# Python V 3.9.0

import datetime
import time

date = datetime.date.today()

if __name__ == "__main__":

    # 13.1

    file = open("today.txt", "wt")
    file.write(str(date))
    file.close()

    # 13.2

    file = open("today.txt", "rt")
    today_string = file.read()
    file.close()
    print(today_string)

    # 13.3

    fmt = "%Y-%m-%d"

    parsed_string = time.strptime(today_string, fmt)

    print(parsed_string)