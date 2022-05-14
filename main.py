import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from printupdate import print_updates
from percentagecalc import percent

import requests
import datetime


def data(i) -> None:  # this is the update function
    axes.cla()

    # test print of dolar
    print_updates()

    # datetime
    dt = datetime.datetime.today()
    today_date = '{}0{}0{}'.format(dt.year, dt.month, dt.day)
    yesterday_date = '{}0{}0{}'.format(dt.year, dt.month, dt.day - 1)
    before_yesterday_date = '{}0{}0{}'.format(dt.year, dt.month, dt.day - 2)

    # days
    before_yesterday_day = '0{}/0{}'.format(dt.day - 2, dt.month)

    # apis
    api1 = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
    api2 = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/?start_date={}&end_date={}'.format(
        yesterday_date, yesterday_date)
    api3 = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/?start_date={}&end_date={}'.format(
        before_yesterday_date, before_yesterday_date)

    # request api
    response = requests.get(api1)
    late_response = requests.get(api2)
    late_late_response = requests.get(api3)

    # set variables/data
    price = response.json()
    yesterday_price = late_response.json()
    before_yesterday_price = late_late_response.json()

    price_updated: float = float(price['USDBRL']['bid'])
    price_yesterday: float = float(yesterday_price[0]['bid'])
    price_before_yesterday: float = float(before_yesterday_price[0]['bid'])

    # draw chart
    global signal
    global percent

    fig_text_string = f'({1}USD) is equal to ({price_updated}BRL)'
    define_signal()
    fig_text2_string = '{}{:.2f}%'.format(signal, percent)
    axes.set_title('USD/BRL', pad=30)
    fig_text.set_text(fig_text_string)
    fig_text2.set_text(fig_text2_string)

    axes.text('today', price_updated, f'{price_updated}', va='top', ha='left')
    axes.text('yesterday', price_yesterday, f'{price_yesterday}', va='top', ha='left')
    axes.text(before_yesterday_day, price_before_yesterday, f'{price_before_yesterday}', va='top', ha='left')
    axes.scatter(before_yesterday_day, price_before_yesterday, s=20)
    axes.scatter('yesterday', price_yesterday, s=20)
    axes.scatter('today', price_updated, s=20)
    plt.grid(True)

    # chart positions/values
    axes.plot([f'{before_yesterday_day}', 'yesterday', 'today'],
              [price_before_yesterday, price_yesterday, price_updated])


def define_signal():
    global signal
    if percent >0: signal = '+'


# datetime
dt = datetime.datetime.today()
today_date = '{}0{}0{}'.format(dt.year, dt.month, dt.day)
yesterday_date = '{}0{}0{}'.format(dt.year, dt.month, dt.day - 1)
before_yesterday_date = '{}0{}0{}'.format(dt.year, dt.month, dt.day - 2)


# FIRST API AND RESPONSES

api1 = 'https://economia.awesomeapi.com.br/json/last/USD-BRL'
api3 = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/?start_date={}&end_date={}'.format(
    before_yesterday_date, before_yesterday_date)
# responses
response = requests.get(api1)
late_late_response = requests.get(api3)

# set variables
price = response.json()
price_updated: float = float(price['USDBRL']['bid'])
before_yesterday_price = late_late_response.json()
price_before_yesterday: float = float(before_yesterday_price[0]['bid'])

# set figure
figure = plt.figure()
axes = figure.add_subplot(1, 1, 1)


# FIG TEXT

# fig text1
fig_text_string = f'({1}USD) is equal to ({price_updated}BRL)'
fig_text = plt.figtext(0.3, 0.9, fig_text_string, fontsize=14)


# fig text2
global percent
percent = percent(price_before_yesterday, price_updated)
global signal
signal = ''
define_signal()
fig_text2_string = '{}{:.2f}%'.format(signal, percent)
fig_text2 = plt.figtext(0.14, 0.94, fig_text2_string, fontsize=14)

# animate
ani = FuncAnimation(figure, data, interval=5000)  # It will update every 5000ms by default

plt.show()
