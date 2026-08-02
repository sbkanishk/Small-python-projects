def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ₹{highest_bid}")


def clear_screen():
    print("\n" * 50)


def get_valid_bid():
    while True:
        try:
            return int(input("What is your bid?: ₹"))
        except ValueError:
            print("Please enter a valid number.\n")


bids = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name: ")
    price = get_valid_bid()
    bids[name] = price

    clear_screen()

    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    clear_screen()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)