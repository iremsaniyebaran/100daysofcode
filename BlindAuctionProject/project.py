from art import logo
print(logo)
users_name_price ={}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    highest_bidder = ""
    for bidder in bidding_record:
        bid_amounth = bidding_record[bidder]
        if bid_amounth > highest_bid:
            highest_bid = bid_amounth
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")



bid_going = True
while bid_going:
    user_name = input("Who makes the bid?")
    user_price = int(input("what is your bid"))
    users_name_price[user_name] = user_price
    keep_going = input("do you wanna add another person? yes or no")

    if keep_going == "no":
        find_highest_bidder(users_name_price)
        keep_going = False
    elif keep_going == "yes":
        print("\n" * 20)

