from collections import namedtuple, defaultdict
from csv import reader
from pprint import pprint

def quantities_ordered():
    d = defaultdict(int)
    with open("data/OrderItems.csv", "r") as opened_csv:
        order_details = reader(opened_csv)
        Order = namedtuple("Order", order_details.__next__())
        for line in order_details:
            order_detail = Order(*line)
            d[order_detail.ProductID] += int(order_detail.Quantity)

    pprint(dict(d))

def main():
    #add code here
    quantities_ordered()
    return

if __name__ == "__main__":
    main()