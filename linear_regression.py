import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression


def get_dates(months_names):
    y0 = 56
    y1 = 95
    m0 = 0
    m1 = 7
    result = []
    for year in range(y0, y1 + 1):
        for month in range(m0, 12):
            if month == 0:
                result.append(str(year))
            else:
                result.append((str(months_names[month % 12]) + "-" + str(year)))
            if year == y1 and (month % 12) == m1:
                break
    return result


def build_graph():
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    lb = get_dates(months)
    x = [range(1, 477)]
    y = []
    x_pred = [range(477, 485)]
    with open('data.csv') as file:
        for line in file:
            y.append(int(line))

    x, y, x_pred = np.array(x), np.array(y), np.array(x_pred)
    x, x_pred = x.reshape(-1, 1), x_pred.reshape(-1, 1)

    model = LinearRegression()
    model.fit(x, y)

    plt.plot(x, y, color='blue', alpha=0.4)
    plt.plot(lb, model.predict(x), color='red')

    plt.plot(x_pred, model.predict(x_pred), color='green')
    plt.xlabel('Year')
    plt.ylabel('Electricity production')
    plt.xticks(rotation='90')
    plt.xticks(range(0, 490, 12))
    # plt.xlim(280, 304)
    plt.grid()
    plt.show()

    print(list(m + ': ' + str(v) for m, v in zip(months, model.predict(x_pred))))
