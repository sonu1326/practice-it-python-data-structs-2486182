from collections import namedtuple
from csv import reader
def main():
    #add code here
    #read data/Customer.csv
    with open("data/Customer.csv", "r") as opened_csv:
        lines = reader(opened_csv)
        Person = namedtuple("Person", next(lines))
        for line in lines:
            person = Person(*line)
            print(person)
    #Create workable objects with each line
    return

if __name__ == "__main__":
    main()