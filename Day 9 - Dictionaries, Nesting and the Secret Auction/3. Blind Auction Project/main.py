# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

from art import logo

print(logo)

def highest_bidder(bidding_dictionary):
    # winner = ""
    # bid = 0

    # for bidder, amount in bidding_dictionary.items():
    #     # bid_amount = bidding_dictionary[bidder]
    #     if amount > bid:
    #         bid = amount
    #         winner = bidder

    # Alternatif
    winner = max(bidding_dictionary, key=bidding_dictionary.get)
    bid = bidding_dictionary[winner]

    print(f"The winner is {winner} with a bid of ${bid}")

continue_bidding = True
bidders = {}
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bidders[name] = price

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if should_continue == 'no':
        continue_bidding = False
        highest_bidder(bidders)
    elif should_continue == 'yes':
        print("\n" * 20)
