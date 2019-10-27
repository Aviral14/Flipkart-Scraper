# Program to retrieve the stored data on the file print it
import pickle
import sys


def print_data():
    """Function to print the data strored in pickle_dir"""

    pickle_dir = sys.argv[1]
    j = 1

    pickle_in = open(pickle_dir, 'rb')
    while True:
        try:
            print(j)
            for i in pickle.load(pickle_in).items():
                print(i)
            j += 1
        except BaseException:
            if j == 1:
                print('Nothing to display')
                print('Enter a valid number of laptops in run.py')
                break
            print('All Laptops Displayed')
            break


print_data()
