# Python V 3.9.0

import termplotlib as tpl

if __name__ == "__main__":

    y_list = input("What are the names for each row (text)? ")
    x_list = input("What are values for each row (name)? ")

    y = []
    x = []

    for i in y_list.split():
        y.append(i)

    for i in x_list.split():
        x.append(float(i))

    fig = tpl.figure()

    fig.barh(x, y)

    fig.show()

