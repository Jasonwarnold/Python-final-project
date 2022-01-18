# ------------------------------------------------------------------
# Class: CIST 2371 Beginning Python Programming
# Term: Spring 2021
# Instructor: Jianmin Wang
# Description: Solution to semester project gas price statistics
# Due: 05/05/2021
# author Jason Arnold
# version 1.0
#
# By turning in this code, I Pledge:
#  1. That I have completed the programming assignment independently.
#  2. I have not copied the code from a student or any source.
#  3. I have not given my code to any student.
#
# ---------------------------------------------------------------------

class Item:
    def __init__(self, month, day, year, price):
        self.__month = month
        self.__day = day
        self.__year = year
        self.price = price

    def __repr__(self):
        return '{' + self.__month + ', ' + self.__day + ', ' + self.__year + ', ' + str(self.price) + '}'

    def set_month(self, month):
        self.__month = month

    def get_month(self):
        return self.__month

    def set_day(self, day):
        self.__day = day

    def get_day(self):
        return self.__day

    def set_year(self, year):
        self.__year = year

    def get_year(self):
        return self.__year

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def display_item(self):
        print(self.__month, '-', self.__day, '-', self.__year, ' : ', '${:,.3f}'.format(self.price), sep='')


records = []
header = '   Date    | Price'
months = {'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May', '06': 'June', '07': 'July',
          '08': 'August', '09': 'September', '10': 'October', '11': 'November', '12': 'December'}


def get_prices():
    global records
    file_name = input('Enter file name to import:  ')
    try:
        with open(file_name, 'r')as file:
            for line in file:
                record = line.split(':')
                date = record[0].split('-')
                month = date[0]
                day = date[1]
                year = date[2]
                price = float(record[1])
                item = Item(month, day, year, price)
                records.append(item)
        print('Prices successfully imported from', file_name)
        input('Press Enter to continue to main menu.')
    except IOError:
        print('File not found.')


def avg_price_per_year():
    global records
    year = records[0].get_year()
    total = 0
    count = 0
    for item in records:
        item_year = item.get_year()
        if item_year == year:
            total += item.get_price()
            count += 1
            if item == records[-1]:
                avg = total / count
                print('Average gas price for', year, 'is', '${:.3f}'.format(avg))
        else:
            avg = total / count
            print('Average gas price for', year, 'is', '${:.3f}'.format(avg))
            total = 0
            count = 0
            year = item.get_year()
    input('Press enter to return to menu.')


def avg_price_per_month():
    global records
    year = '1993'
    month = '04'
    total = 0
    count = 0
    for item in records:
        item_year = item.get_year()
        if item_year == year:
            item_month = item.get_month()
            if item_month == month:
                total += item.get_price()
                count += 1
                if item == records[-1]:
                    avg = total / count
                    print('Average gas price for', months[month], year, 'is', '${:.3f}'.format(avg))
            else:
                avg = total / count
                print('Average gas price for', months[month], year, 'is', '${:.3f}'.format(avg))
                total = 0
                count = 0
                year = item.get_year()
                month = item.get_month()
        else:
            year = item.get_year()
    input('Press Enter to return to menu.')


def high_low_per_year():
    global records
    year = '1993'
    prices = []
    for item in records:
        item_year = item.get_year()
        if item_year == year:
            prices.append(item.get_price())
            if item == records[-1]:
                print('Highest gas price in', year, 'is', max(prices))
                print('Lowest gas price in', year, 'is', min(prices))
        else:
            print('Highest gas price in', year, 'is', max(prices))
            print('Lowest gas price in', year, 'is', min(prices))
            prices = []
            year = item.get_year()
    input('Press Enter to return to menu.')


def list_low_to_high():
    global records
    records.sort(key=lambda x: x.price)
    with open('priceslowtohigh.txt', 'w') as file:
        for item in records:
            string = item.get_month() + '-' + item.get_day() + '-' + item.get_year() + ':' + str(item.get_price()) + \
                     '\n'
            file.write(string)
    print('Records sorted lowest to highest price, saved to file \'priceslowtohigh.txt\'')
    input('Press Enter to return to menu.')


def list_high_to_low():
    global records
    records.sort(key=lambda x: x.price, reverse=True)
    with open('priceshightolow.txt', 'w') as file:
        for item in records:
            string = item.get_month() + '-' + item.get_day() + '-' + item.get_year() + ':' + str(item.get_price()) + \
                     '\n'
            file.write(string)
    print('Records sorted highest to lowest price, saved to file \'priceshightolow.txt\'')
    input('Press Enter to return to menu.')


def main():
    run = True
    get_prices()
    while run:
        print('Select from the following options: ')
        print('1. Show average price per year.')
        print('2. Show average price per month.')
        print('3. Show the highest and lowest prices for each year.')
        print('4. Export prices sorted lowest to highest.')
        print('5. Export prices sorted highest to lowest.')
        print('6. Exit')
        choice = input('Selection:  ')
        if choice == '1':
            avg_price_per_year()
        elif choice == '2':
            avg_price_per_month()
        elif choice == '3':
            high_low_per_year()
        elif choice == '4':
            list_low_to_high()
        elif choice == '5':
            list_high_to_low()
        elif choice == '6':
            run = False
        else:
            print('Invalid selection')


main()
