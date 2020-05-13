#!/usr/bin/python

import argparse

def find_max_profit(prices):
    best = -(prices[0])
    for i in range(0, len(prices)):
        cost = -(prices[i])
        for j in range(i+1, len(prices)):
            profit = cost + prices[j]
            if profit > best:
                best = profit
    return best



if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))