# Currency Converter

import requests

url = str.__add__('http://data.fixer.io/api/latest?access_key=',
                  '5934bf3f2adef071c95f87d808b3bb28')


class CurrencyConverter:
    # empty dict to store the conversion rates
    rates = {}

    def __init__(self, url):
        data = requests.get(url).json()
        self.rates = data["rates"]

    def convert(self, from_currency, to_currency, amount):
        if from_currency != 'EUR':
            amount = amount / self.rates[from_currency]

        # limiting the precision to 2 decimal places
        amount = round(amount * self.rates[to_currency], 2)
        return amount


# Set to 1 when file is being written
file_handling_flag = 0

# USD to INR conversion


class usd_inr(CurrencyConverter):

    def __init__(self, x):
        super().__init__(url)
        self.x = self.convert("USD", "INR", 1)

    def conversion(self, amount):
        try:
            assert amount > 0
            USD = amount * self.x
            if(file_handling_flag == 0):
                print("The amount in INR is: ", "{0:.2f}".format(USD))
            else:
                test_obj1 = input_output_file()
                test_obj1. testing_write("USD", "INR", amount,
                                         "{0:.2f}".format(USD))
        except AssertionError:
            print("Invalid input")

# INR to USD conversion


class inr_usd(usd_inr):

    def conversion(self, amount):
        try:
            assert amount > 0
            INR = amount/self.x
            if(file_handling_flag == 0):
                print("The amount in USD is: ", "{0:.2f}".format(INR))
            else:
                test_obj1 = input_output_file()
                test_obj1.testing_write("INR", "USD", amount,
                                        "{0:.2f}".format(INR))
        except AssertionError:
            print("Invalid input")

# EURO to INR conversion


class euro_inr(CurrencyConverter):

    def __init__(self, x):
        super().__init__(url)
        self.x = self.convert("EUR", "INR", 1)

    def conversion(self, amount):
        try:
            assert amount > 0
            EURO = amount*self.x
            if(file_handling_flag == 0):
                print("The amount in INR is: ", "{0:.2f}".format(EURO))
            else:
                test_obj1 = input_output_file()
                test_obj1.testing_write("EURO", "INR", amount,
                                        "{0:.2f}".format(EURO))
        except AssertionError:
            print("Invalid input")

# INR to EURO conversion


class inr_euro(euro_inr):

    def conversion(self, amount):
        try:
            assert amount > 0
            INR = amount/self.x
            if(file_handling_flag == 0):
                print("The amount in EURO is: ", "{0:.2f}".format(INR))
            else:
                test_obj1 = input_output_file()
                test_obj1.testing_write("INR", "EURO", amount,
                                        "{0:.2f}".format(INR))

        except AssertionError:
            print("Invalid input")

# EURO to USD conversion


class euro_usd(CurrencyConverter):

    def __init__(self, x):
        super().__init__(url)
        self.x = self.convert("EUR", "USD", 1)

    def conversion(self, amount):
        try:
            assert amount > 0
            EURO = amount*self.x
            if(file_handling_flag == 0):
                print("The amount in USD is: ", "{0:.2f}".format(EURO))
            else:
                test_obj1 = input_output_file()
                test_obj1.testing_write("EURO", "USD", amount,
                                        "{0:.2f}".format(EURO))
        except AssertionError:
            print("Invalid input")

# USD to EURO conversion


class usd_euro(euro_usd):

    def conversion(self, amount):
        try:
            assert amount > 0
            USD = amount/self.x
            if(file_handling_flag == 0):
                print("The amount in EURO is: ", "{0:.2f}".format(USD))
            else:
                test_obj1 = input_output_file()
                test_obj1.testing_write("USD", "EURO", amount,
                                        "{0:.2f}".format(USD))
        except AssertionError:
            print("Invalid input")


# File Handling for testing


class input_output_file:

    def testing_read(self):
        fr = open("inputfile.txt", "r")
        for line in fr:
            option = int(line[0])
            value = ''
            for i in range(2, len(line)):
                value = value + line[i]
            value = float(value)
            menu(option, value, url)
        fr.close()

    def testing_write(self, curr1, curr2, given_value, conv_value):
        fw = open("outputfile.txt", "a")
        output_str = str(str(given_value) + " " + curr1 + " --> " +
                         curr2 + " " + str(conv_value) + "\n")
        fw.write(output_str)
        fw.close()

# Menu function


def menu(x, amount, url):
    if (x == 1):
        obj = usd_inr(url)
        obj.conversion(amount)
    elif (x == 2):
        obj = inr_usd(x)
        obj.conversion(amount)
    elif (x == 3):
        obj = euro_inr(url)
        obj.conversion(amount)
    elif (x == 4):
        obj = inr_euro(x)
        obj.conversion(amount)
    elif (x == 5):
        obj = euro_usd(url)
        obj.conversion(amount)
    elif (x == 6):
        obj = usd_euro(url)
        obj.conversion(amount)
    elif (x > 8):
        print("Invalid choice !!!")


print("     \t\t\tCURRENCY CONVERTER     \n\n")
print("Options:")
print("\t1. USD   --->  INR")
print("\t2. INR   --->  USD")
print("\t3. EURO  --->  INR")
print("\t4. INR   --->  EURO")
print("\t5. EURO  --->  USD")
print("\t6. USD   --->  EURO")
print("\t7. Testing file handling")

value = int(input("Enter your choice "))
if(value < 7):
    amount = float(input("Enter amount to be converted: "))
    menu(value, amount, url)
if(value == 7):
        test_obj = input_output_file()
        file_handling_flag = 1
        test_obj.testing_read()
        print("\noutputfile.txt updated using inputs from inputfile.txt\n")
